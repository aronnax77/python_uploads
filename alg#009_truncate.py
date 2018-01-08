"""
reverse_string.py
Author: Richard Myatt
Date: 8 January 2018

This is an algorithm which mirrors a question set for JS.  The challenge in this
case is to truncate a string (str) by the integer (num).  The truncated string is
to be returned with ... appended.  In such cases the three dots will add to the
strings length.  However if the given maximum string length (num) is less than or
equal to three the addition of the three dots will not be counted as part of the
strings length.

Test cases are as follows:

 should return "A-tisket...".
truncateString("Peter Piper picked a peck of pickled peppers", 14) should return "Peter Piper...".
truncateString("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length) should return "A-tisket a-tasket A green and yellow basket".
truncateString("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length + 2) should return "A-tisket a-tasket A green and yellow basket".
truncateString("A-", 1) should return "A...".
truncateString("Absolutely Longer", 2) should return "Ab...".

Please enter a string and a number on a separate line at the prompt.  For instance

"""

def truncateString(str, num):
    if num >= len(str):
        return str;
    elif num <= 3:
        return str[0:num] + '...'
    else:
        return str[0:num-3] + '...'

text   = input()
number = int(input())
print(truncateString(text, number))
