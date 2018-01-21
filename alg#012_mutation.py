"""
mutation.py
Author: Richard Myatt
Date: 15 January 2018

This is an exercise which mirrors a question set for JS.  Write a function that
returns true if the string in the first element of the array argument contains all
of the letters of the string in the second element of the array.

Test cases:

mutation(["hello", "hey"]) should return false.
mutation(["hello", "Hello"]) should return true.
mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]) should return true.
mutation(["Mary", "Army"]) should return true.
mutation(["Mary", "Aarmy"]) should return true.
mutation(["Alien", "line"]) should return true.
mutation(["floor", "for"]) should return true.
mutation(["hello", "neo"]) should return false.
mutation(["voodoo", "no"]) should return false.

The second of these cases is used if you run the code below.  Please feel free to
substitute any of the other test cases or one of your own.

"""

def mutation(arr):
    firstLower  = arr[0].lower()
    secondLower = arr[1].lower()

    for letter in secondLower:
        if letter not in firstLower:
            return False

    return True

print(mutation(["hello", "Hello"]))
