#!/usr/bin/python3

#############################################################################################
#                                                                                           #
#	PLEASE NOTE THAT THIS CODE WILL NOT RUN IN THE SOLOLEARN CODE PLAYGROUND.               # 
#                                                                                           #
#	This is a cgi test script written in python.  To see this code in action it will be     #
#	necessary to run a server.  This is possible through a local server like apache but     #
#	can also be achieved through a server written in python.  The code for such a server is #
#	shown here xxxxxxxxxxxxxxx for those who may be interested.                             #
#                                                                                           #
#############################################################################################

text1 = """Content-type: text/html\n
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CGI 101</title>
</head>
<body>

<H1>A Third CGI Script</H1>
<HR>
<P>Hello, CGI World!</P>

<table>
"""

print(text1)

for i in range(5):
    print('<tr>')
    for j in range(4):
        print('<td>%d.%d</td>' % (i, j))
    print('</tr>')

print("""
</table>

</body>
</html>""")
