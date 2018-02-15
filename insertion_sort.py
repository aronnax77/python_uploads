""" Author: Richard Myatt
    Date: 15 February 2018

    The function below represents an implementation of the 'insertion sort'
    algorithm.  This is demonstrated with the list [33, 20, 12, 31, 2, 67]
    but should work with any other list.
"""

def insertionSort(l):
    """
    An implementation of insertion sort
    """
    result = l[:]

    lengthData = len(result)
    start = 1

    while start <= lengthData - 1:
        if result[start] < result[start - 1]:
            value = result.pop(start)

            # find insertion point
            for i in range(start):
                if result[i] > value:
                    result.insert(i, value)
                    break
        start += 1

    return result


print(insertionSort([33, 20, 12, 31, 2, 67]))
