#!/usr/bin/python
#http://www.tutorialspoint.com/python/python_cgi_programming.htm

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('maths'):
   math_flag = "ON"
else:
   math_flag = "OFF"

if form.getvalue('physics'):
   physics_flag = "ON"
else:
   physics_flag = "OFF"


print("Content-type:text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Hello - Third CGI Program</title>
        </head>
        <body>
        """)
print ("<h2> CheckBox Maths is : %s</h2>" % math_flag)
print ("<h2> CheckBox Physics is : %s</h2>" % physics_flag)
print('''<form action="/cgi-bin/checkbox.py" method="POST" target="_blank">
        <input type="checkbox" name="maths" value="on" /> Maths
        <input type="checkbox" name="physics" value="on" /> Physics
        <input type="submit" value="Select Subject" />
        </form>

        </body>
        </html>
        ''')
