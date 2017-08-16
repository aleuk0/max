#!/usr/bin/python
#http://www.tutorialspoint.com/python/python_cgi_programming.htm

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('subject'):
    subject = form.getvalue('subject')
else:
    subject = "Not set"

print("Content-type:text/html\n")
print('''<!DOCTYPE HTML>
        <html>
        <head>
        <title>Radio - Fourth CGI Program</title>
        </head>
        <body>
        ''')
print("<h2> Selected Subject is %s</h2>" % subject)
print('''<form action="/cgi-bin/radio.py" method="post" target="_blank">
        <input type="radio" name="subject" value="maths" /> Maths
        <input type="radio" name="subject" value="physics" /> Physics
        <input type="submit" value="Select Subject" />
        </form>

        </body>
        </html>
        ''')
