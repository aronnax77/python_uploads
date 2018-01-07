"""
largest.py
Author: Richard Myatt
Date: 5 January 2018

Return an array consisting of the largest number from each provided sub-array.
For simplicity, the provided array will contain exactly 4 sub-arrays.

This is an algorithm which mirrors a question set for JS.

A sample set of lists is provided for this example being:
[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]

"""

def largestOfFour(arrList):
    result  = []
    maxItem = 0
    for each in arrList:
        maxItem = max(each)
        result.append(maxItem)

    return result


arr = [4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]
print(largestOfFour(arr))
