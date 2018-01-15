"""
chunky.py
Author: Richard Myatt
Date: 15 January 2018

This is an algorithm which mirrors a question set for JS.  Write a function that
splits an array (first argument) into groups the length of size (the second argument)
and returns them as a two-dimensional array.

Please enter an array (list) of numbers followed by a positive integer at the prompt.
For instance if you enter the list 0 1 2 3 4 5 6 7 8 followed by 2 the
result should be [[0, 1], [2, 3], [4, 5], [6, 7], [8]].

"""

def chunkArrayInGroups(arr, size):
    newArr = []
    i = 0
    while i < len(arr):
        newArr.append(arr[i : i + size])
        i += size

    return newArr

numList = [int(x) for x in input().split()]
chunkSize = int(input())
print(chunkArrayInGroups(numList, chunkSize))


#print(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2))
