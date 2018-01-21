"""
belong.py
Author: Richard Myatt
Date: 21 January 2018

This is an exercise which mirrors a question set for JS.  Return the lowest
index at which a value (second argument) should be inserted into an array
(first argument) once it has been sorted. The returned value should be a number.

For example, getIndexToIns([1,2,3,4], 1.5) should return 1 because it is greater
than 1 (index 0), but less than 2 (index 1).

Likewise, getIndexToIns([20,3,5], 19) should return 2 because once the array has
been sorted it will look like [3,5,20] and 19 is less than 20 (index 2) and
greater than 5 (index 1).

Test cases:

getIndexToIns([10, 20, 30, 40, 50], 35) should return 3.
getIndexToIns([10, 20, 30, 40, 50], 30) should return 2.
getIndexToIns([40, 60], 50) should return 1.
getIndexToIns([3, 10, 5], 3) should return 0.
getIndexToIns([5, 3, 20, 3], 5) should return 2.
getIndexToIns([2, 20, 10], 19) should return 2.
getIndexToIns([2, 5, 10], 15) should return 3.

Test case 2 of the above is used in the code below.  Please feel free to substitute
any of the other test cases or one of your own.

"""

def getIndexToIns(arr, num):
    arrCopy = arr
    arrCopy.sort()
    index = 0

    if num <= arrCopy[index]:
        return 0
    elif num > arrCopy[len(arrCopy) - 1]:
        return len(arrCopy)

    while index < len(arrCopy) - 1:
        if num > arrCopy[index] and num <= arrCopy[index + 1]:
            return index + 1
        else:
            index += 1


print(getIndexToIns([10, 20, 30, 40, 50], 30))
