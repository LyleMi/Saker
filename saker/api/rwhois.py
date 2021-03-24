import socket
import cfscrape
import requests
from bs4 import BeautifulSoup

# reverse whois: get domain by whois info

class RWhois(object):

    url = "https://viewdns.info/"
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'

    def __init__(self):
        super(RWhois, self).__init__()
        self.s = requests.Session()
        self.get_cf_cookies()

    def get_cf_cookies(self):
        tokens, user_agent = cfscrape.get_tokens(self.url, self.useragent)
        print(tokens, user_agent)
        for key in tokens:
            self.s.cookies.set(key, tokens[key])

    def query(self, domain):
        api = "reversewhois/?q="
        headers = {
            'User-Agent': self.useragent
        }
        r = self.s.get(self.url + api + domain, headers=headers)
        if r.ok:
            soup = BeautifulSoup(r.content, 'html.parser')
            domain_table = soup('table')[3]
            domain_list = [row('td')[0].string for row in domain_table.findAll('tr')]
            if domain_list and domain_list[0] is not None:
                domain_list.remove("Domain Name")  # filter the header
        else:
            print("reverse whois api error")
            print(r.text)
            domain_list = []
        if None in domain_list:
            domain_list.remove(None)
        return domain_list
