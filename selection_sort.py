""" Author: Richard Myatt
    Date: 16 February 2018

    The function below represents an implementation of the 'selection sort'
    algorithm.  This is demonstrated with the list [33, 20, 12, 31, 2, 67]
    but should work with any other list.
"""



def selectionSort(l):
    """
    An implementation of selection sort
    """
    result = l[:]

    for elementIndex in range((len(result) - 1)):
        value = result[elementIndex]
        lowerIndex = elementIndex
        swapIndex  = None
        while lowerIndex < len(result):
            if result[lowerIndex] < value:
                value = result[lowerIndex]
                swapIndex = lowerIndex
            lowerIndex += 1
        if value != result[elementIndex]:
            result[swapIndex] = result[elementIndex]
            result[elementIndex] = value

    return result



print(selectionSort([33, 20, 12, 31, 2, 67]))
