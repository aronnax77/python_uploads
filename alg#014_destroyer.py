"""
destroyer.py
Author: Richard Myatt
Date: 20 January 2018

This is an exercise which mirrors a question set for JS.  You will be provided
with an initial array (the first argument in the destroyer function), followed
by one or more arguments. Remove all elements from the initial array that are
of the same value as these arguments.

Test cases:

destroyer([1, 2, 3, 1, 2, 3], 2, 3) should return [1, 1].
destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3) should return [1, 5, 1].
destroyer([3, 5, 1, 2, 2], 2, 3, 5) should return [1].
destroyer([2, 3, 2, 3], 2, 3) should return [].
destroyer(["tree", "hamburger", 53], "tree", 53) should return ["hamburger"].

The code below uses the second case above.  Please feel free to use any other
test case or substitute one of your own.

"""

def destroyer(arr, *args):
    arrCopy = arr
    toRemove = list(args)
    for item in toRemove:
        while item in arr:
            arrCopy.remove(item)

    return arrCopy


print(destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3))
