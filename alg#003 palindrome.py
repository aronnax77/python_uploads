"""
palindrome.py
Author: Richard Myatt
Date: 2 January 2018

This is an algorithm which mirrors a question set for JS.

Write a function palindrome(str) to return true if a string
is a palindrome, otherwise return false.  For the purpose of this exercise a
palindrome is a word or sentence that is spelled the same way both forward
and backward, ignoring punctuation, case and spacing.

Please enter a test string at the prompt
"""

import re

def palindrome(str):
    # remove all non alphanumeric characters
    newStr = re.sub(r'\W+', '', str)
    if newStr.lower() == newStr.lower()[::-1]:
        return True
    else:
        return False

testText = input()

result   = palindrome(testText)
if(result == True):
	print("The test string you entered is a palindrome.")
else:
	print("The test string you entered is not a palindrome.")
