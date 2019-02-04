#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import json
import requests
from bs4 import BeautifulSoup


class WebPage(object):
    """
    Simple representation of a web page
    """

    def __init__(self, url):
        """
        Initialize a new WebPage object.
        """
        response = requests.get(url, verify=False, timeout=30)
        self.url = url
        self.html = response.text
        self.headers = response.headers

        soup = BeautifulSoup(self.html, "html.parser")
        self.scripts = [script['src'] for script in
                        soup.findAll('script', src=True)]
        self.meta = {
            meta['name'].lower():
                meta['content'] for meta in soup.findAll(
                    'meta', attrs=dict(name=True, content=True))
        }

        self.title = soup.title.string if soup.title else 'None'
        self.apps = Wappalyzer().analyze(self)

    def info(self):
        return {
            "apps": self.apps,
            "title": self.title,
        }


class Wappalyzer(object):
    """
    Python Wappalyzer driver.
    """

    def __init__(self):
        appurl = 'https://raw.githubusercontent.com/AliasIO/Wappalyzer/master/src/apps.json'
        apppath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "apps.json")
        if not os.path.exists(apppath):
            with open(apppath, 'wb') as fd:
                fd.write(requests.get(appurl).content)
        with open(apppath, 'rb') as fd:
            obj = json.load(fd)

        self.categories = obj['categories']
        self.apps = obj['apps']

        for name, app in self.apps.items():
            self._prepare_app(app)

    def _prepare_app(self, app):
        """
        Normalize app data, preparing it for the detection phase.
        """

        # Ensure these keys' values are lists
        for key in ['url', 'html', 'script', 'implies']:
            value = app.get(key)
            if value is None:
                app[key] = []
            else:
                if not isinstance(value, list):
                    app[key] = [value]

        # Ensure these keys exist
        for key in ['headers', 'meta']:
            value = app.get(key)
            if value is None:
                app[key] = {}

        # Ensure the 'meta' key is a dict
        obj = app['meta']
        if not isinstance(obj, dict):
            app['meta'] = {'generator': obj}

        # Ensure keys are lowercase
        for key in ['headers', 'meta']:
            obj = app[key]
            app[key] = {k.lower(): v for k, v in obj.items()}

        # Prepare regular expression patterns
        for key in ['url', 'html', 'script']:
            app[key] = [self._prepare_pattern(pattern) for pattern in app[key]]

        for key in ['headers', 'meta']:
            obj = app[key]
            for name, pattern in obj.items():
                obj[name] = self._prepare_pattern(obj[name])

    def _prepare_pattern(self, pattern):
        """
        Strip out key:value pairs from the pattern and compile the regular
        expression.
        """
        regex, _, rest = pattern.partition('\\;')
        try:
            return re.compile(regex, re.I)
        except re.error as e:
            # regex that never matches:
            # http://stackoverflow.com/a/1845097/413622
            return re.compile(r'(?!x)x')

    def _has_app(self, app, webpage):
        """
        Determine whether the web page matches the app signature.
        """
        # Search the easiest things first and save the full-text search of the
        # HTML for last

        for regex in app['url']:
            if regex.search(webpage.url):
                return True

        for name, regex in app['headers'].items():
            if name in webpage.headers:
                content = webpage.headers[name]
                if regex.search(content):
                    return True

        for regex in app['script']:
            for script in webpage.scripts:
                if regex.search(script):
                    return True

        for name, regex in app['meta'].items():
            if name in webpage.meta:
                content = webpage.meta[name]
                if regex.search(content):
                    return True

        for regex in app['html']:
            if regex.search(webpage.html):
                return True

    def _get_implied_apps(self, detected_apps):
        """
        Get the set of apps implied by `detected_apps`.
        """
        def __get_implied_apps(apps):
            _implied_apps = set()
            for app in apps:
                if 'implies' in self.apps[app]:
                    _implied_apps.update(set(self.apps[app]['implies']))
            return _implied_apps

        implied_apps = __get_implied_apps(detected_apps)
        all_implied_apps = set()

        # Descend recursively until we've found all implied apps
        while not all_implied_apps.issuperset(implied_apps):
            all_implied_apps.update(implied_apps)
            implied_apps = __get_implied_apps(all_implied_apps)

        return all_implied_apps

    def get_categories(self, app_name):
        """
        Returns a list of the categories for an app name.
        """
        cat_nums = self.apps.get(app_name, {}).get("cats", [])
        cat_names = [self.categories.get("%s" % cat_num, "")
                     for cat_num in cat_nums]

        return cat_names

    def analyze(self, webpage):
        """
        Return a list of applications that can be detected on the web page.
        """
        detected_apps = set()

        for app_name, app in self.apps.items():
            if self._has_app(app, webpage):
                detected_apps.add(app_name)

        detected_apps |= self._get_implied_apps(detected_apps)

        return detected_apps
