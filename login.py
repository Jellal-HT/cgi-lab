#!/usr/bin/env python3

import cgi
import os
from templates import login_page
from templates import secret_page
import secret

def parse_cookies(cookie_string):
    result = {}
    if cookie_string == "":
        return result
    for cookie in cookies:
        split_cookie = cookie.split("=")
        result[split_cookie[0]] = split_cookie[1]
    return result

form = cgi.FieldStorage()
cookies = parse_cookies(os.environ["HTTP_COOKIE"])
username = form.getfirst("username")
password = form.getfirst("password")


header = ""
header += "Content-Type: text/html\r\n"    
body = ""

if username == secret.username and password == secret.password:
    body += secret_page(username, password)
    header += "Set-Cookie: logged=true; Max-Age=60\r\n"
    header += "Set-Cookie: cookie=nom\r\n"
    body += "<h1>A terrible secret</h1>"
else:
    body += login_page()

print(header)
print()
print(body)
