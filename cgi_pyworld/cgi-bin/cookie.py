#!/usr/bin/env python3

# print("Set-cookie: name=value; expires=Wed May 18 03:33:20 2033;
#        path=/cgi-bin/; httponly")     # можно не писать дату, тогда будут
                                        # храниться до выключения браузера

import os
import http.cookies

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
