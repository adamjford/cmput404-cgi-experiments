#!/usr/bin/env python

import os, json, cgi, Cookie

form = cgi.FieldStorage()

username = form.getvalue('user')
password = form.getvalue('password')

C = Cookie.SimpleCookie()
C.load(os.environ["HTTP_COOKIE"])

print "Content-Type: text/html"
if username == "bob" and password == "hunter2":
    print "Set-Cookie: loggedin=true"
print

print "<!DOCTYPE html>"
print "<html><body>"
print "<h1>Hello World!</h1>"
print "Your magic tracking number is:"
print form.getvalue('magic_tracking_number')
print "<p>Your Browser is"
if "Firefox" in os.environ['HTTP_USER_AGENT']:
    print "Firefox!"
elif "Chrome" in os.environ['HTTP_USER_AGENT']:
    print "Chrome!"
else:
    print os.environ['HTTP_USER_AGENT']
print "</p>"

print "<form method='post'><input name='user'><input type='password' name='password'>"
print "<input type='submit'></form>"

print "<p>Username: " + str(username) + "</p>"
print "<p>Password: " + str(password) + "</p>"

if username == "bob" and password == "hunter2":
    print "<p>Login Successful!</p>"

if 'loggedin' in C:
    print "<p>loggedin=" + C["loggedin"].value + "</p>"
else:
    print "<p>No cookie!</p>"

print "</body></html>"

