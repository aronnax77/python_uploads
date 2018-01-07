"""
repeatString.py
Author: Richard Myatt
Date: 7 January 2018

This is an algorithm which mirrors a question set for JS.

The challenge in this case was to write out a string repeated a number of times.
This is a trivial exercise in python as shown below.

Please enter a string at the prompt followed by an integer number on a separate line.

"""

def repeatStringNum(str, num):
    return str * num


inputString = input()
number      = int(input())

print(repeatStringNum(inputString, number))
