"""
factorial.py
Author: Richard Myatt
Date: 28 October 2017

This is an algorithm which mirrors a question set for JS.  The challenge is to return the 
factorial of a given positive integer.

Please enter a positive integer at the prompt.  For instance if you enter 6 the result should
be 720.

"""

def myFactorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * myFactorial(num - 1)

n = int(input())
print("The factorial of %d is %d" % (n, myFactorial(n)))
