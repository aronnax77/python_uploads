""" Author: Richard Myatt
    Date: 14 February 2018

    The function below represents the implementation of the 'bubble sort'
    algorithm.  This is demonstrated with the list [33, 20, 12, 31, 2, 67]
    but should work with any other list.
"""

def bubbleSort(l):
    """
    An implementation of the bubble sore with optimisation
    """
    result = l[:]

    lengthData = len(result)
    sweep      = lengthData - 1

    while sweep >= 0:
        for i in range(sweep):
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]
        sweep -= 1

    return result


print(bubbleSort([33, 20, 12, 31, 2, 67]))
