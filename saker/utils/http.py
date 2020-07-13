from http.cookies import SimpleCookie


def loadCookie(rawdata):
    cookie = SimpleCookie()
    cookie.load(rawdata)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies
