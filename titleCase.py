"""
titleCase.py
Author: Richard Myatt
Date: 4 January 2018

This is an algorithm which mirrors a question set for JS.

Please enter a string at the prompt.  For instance if you enter
'This is a brand new year.' the sentence should be returned as
'This Is A Brand New Year.'

"""

def titleCase(aString):
    return aString.title()

text = input()
print(titleCase(text))
