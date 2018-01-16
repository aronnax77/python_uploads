"""
slasher.py
Author: Richard Myatt
Date: 16 January 2018

This is a problem which mirrors a question set for JS.  Write a function to return
the remaining elements of an array after chopping off n elements from the head.

Please enter an array (list) on one line at the prompt followed by a positive digit
on the next line.  For instance if you enter 1 2 3 on one line as the array (list)
then 2 on the next line the return value should be [3].

"""

def slasher(arr, howMany):
    return arr[howMany : ]


array  = [int(x) for x in input().split()]
number = int(input())
print(slasher(array, number))
