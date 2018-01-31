"""
cipher.py
Author: Richard Myatt
Date: 22 January 2018

This is an exercise which mirrors a question set for JS.  One of the simplest
and most widely known ciphers is a Caesar cipher, also known as a shift cipher. In a shift cipher the meanings of the letters are shifted by some set amount.

A common modern use is the ROT13 cipher, where the values of the letters are
shifted by 13 places. Thus 'A' ↔ 'N', 'B' ↔  'O' and so on.

Write a function which takes a ROT13 encoded string as input and returns a
decoded string.

All letters will be uppercase. Do not transform any non-alphabetic character
(i.e. spaces, punctuation), but do pass them on.

Test cases:

rot13("SERR PBQR PNZC") should decode to "FREE CODE CAMP"
rot13("SERR CVMMN!") should decode to "FREE PIZZA!"
rot13("SERR YBIR?") should decode to "FREE LOVE?"
rot13("GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.") should decode to
"THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX."

The code below uses the last of these test cases.  Please feel free to substitute
any of the other test cases or use your own.

"""

alphabet = ''.join([chr(num) for num in range(65, 91)])
# alphabet.split(', ')

def decodeRot13Char(ch):
    if ch == ' ' or ch == '!' or ch == '.' or ch == ',' or ch == '?':
        return ch
    else:
        i = alphabet.index(ch) - 13
        if i < 0:
            i += 26
    return alphabet[i]

def rot13(coded):
    strList = list(coded)
    result = ''.join(list(map(decodeRot13Char, strList)))
    return result

print(rot13("GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK."))
