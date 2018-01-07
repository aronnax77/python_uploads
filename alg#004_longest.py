"""
capitalize.py
Author: Richard Myatt
Date: 3 January 2018

This is an algorithm which mirrors a question set for JS.

Return the length (as a number) of the longest word in the
sentence which forms the argument of the function findLongestWord(str).

Please enter a test string at the prompt
"""

import re

def findLongestWord(str):
    pattern = re.compile('\S+')
    words = pattern.findall(str)

    wordLength = 0
    for word in words:
        if len(word) > wordLength:
            wordLength = len(word)

    return wordLength

text = input()
result = findLongestWord(text)
print("The longest word in the string has a length of %s" % result)

#print(findLongestWord("The quick brown fox jumped over the lazy dog"))
