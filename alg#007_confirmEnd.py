"""
confirmEnd.py
Author: Richard Myatt
Date: 6 January 2018

This is an algorithm which mirrors a question set for JS.  Confirm the ending of
the string 'str', with the 'target' using substrings and not the python endsWith()
function.

Please enter two strings at the prompt on two separate lines.  For instance if
you enter - Bastian - as the first string and - n - as the second string then the
function should return - True.

"""

def confirmEnding(str, target):
    strLength    = len(str)
    targetLength = len(target)
    sliceStart   = strLength - targetLength
    if(target == str[sliceStart : ]):
        return True
    else:
        return False

inputStr    = input()
inputTarget = input()

print(confirmEnding(inputStr, inputTarget))
