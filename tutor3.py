#!/usr/bin/python3

#############################################################################################
#                                                                                           #
#	PLEASE NOTE THAT THIS CODE WILL NOT RUN IN THE SOLOLEARN CODE PLAYGROUND.               # 
#                                                                                           #
#	This is a cgi test script written in python.  To see this code in action it will be     #
#	necessary to run a server.  This is possible through a local server like apache but     #
#	can also be achieved through a server written in python.  The code for such a server is #
#	shown here xxxxxxxxxxxxxxx for those who may be interested.                             #
#
#	This script can be called with the data/query field ?user=John
#                                                                                           #
#############################################################################################

import cgi
#import cgitb
#cgitb.enable()
form = cgi.FieldStorage()           # parse form data
print('Content-type: text/html')    # plus blank line

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>tutor3.py</title>
</head>
<body>
  <h1>Greetings</h1>
  <hr>
  <p>%s</p>
  <hr>
</body>
</html>"""

if not 'user' in form:
    print(html % 'Who are you?')
else:
    print(html % ('Hello, %s' % form['user'].value))
