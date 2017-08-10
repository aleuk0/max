#!/usr/bin/python
#http://www.tutorialspoint.com/python/python_cgi_programming.htm

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

print("Content-type:text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Hello - Second CGI Program</title>
        </head>

        <body>
        <form action="/cgi-bin/hello_get.py" method="get">
        First Name: <input type="text" name="first_name">  <br />
        Last Name: <input type="text" name="last_name" />
        <input type="submit" value="Submit" />
        </form>
        """)

print("<h2>Hello {} {}</h2>".format(first_name, last_name))

print("""</body>
        </html>""")
