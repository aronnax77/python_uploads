"""
reverse_string.py
Author: Richard Myatt
Date: 28 October 2017

This is an algorithm which mirrors a question set for JS.  Please enter a string 
at the prompt.

"""

# Function to reverse a string
def reverseString(str):
    return str[::-1]


text = input("Please enter a string: ")

print("The string you entered is:     %s" % text)
print("The reverse of this string is: %s" % reverseString(text))
