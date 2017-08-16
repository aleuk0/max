#!/usr/bin/env python3

import os, http.cookies, cgi, cgitb

form = cgi.FieldStorage()

a = 0

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")

if name is None:
    print("Set-cookie: name=Cookie N1")
    print("Content-type: text/html\n")
    print("Cookies!!!")
else:
    print("Content-type: text/html\n")
    print("Cookies:")
    print(name.value)

print("Content-type:text/html\n")
print('''<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Hello - Second CGI Program</title>
        </head>

        <body>
        <form action="/cgi-bin/hello.py" method="post">
        <input type="submit" value="Yes" />
        </form>
        <form action="/cgi-bin/hello.py" method="post">
        <input type="submit" value="No" />
        </form>
        ''')

print("<h2> Variable is : {} </h2>".format(a))

print("""</body>
        </html>""")
