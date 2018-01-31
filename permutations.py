"""

    Author: Richard Myatt
    Date: 28 January 2018

The code below provides a function 'permutations(str)' which will return a list
of the permutations of the letters in the string provided as an argument to the
function.  If there are n letters in the string then the number of permutations
is given by n! so that for strings in excess of four characters the list becomes
large.

The example below returns a list of the permutations of the string 'abc' and
returns ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'].

Please feel free to substiture any other string of your choosing.

"""

# function which will return the permutations of the string 'str'.  Please note
# that the startIndex should be left at its default value.
def permutations(str, startIndex = 0):
    result = []
    i = startIndex

    if startIndex == len(str) - 1:
        result.append(str)
        return result
    else:
        while(i < len(str)):
            newStr = swap(str, startIndex, i)
            for each in permutations(newStr, startIndex + 1):
                result.append(each)
            str = swap(str, startIndex, i)
            i += 1

        return result


# swap is a helper function for the function peremutations and swaps the two
# characters of str whose indecies are given by first and second.  If both
# indecies are the same str is returned in its original form
def swap(str, first, second):

    if first == second:
        return str
    else:
        tempStr = list(str)
        temp    = tempStr[first]
        tempStr[first] = tempStr[second]
        tempStr[second] = temp
        return ''.join(tempStr)



print(permutations('abc'))
