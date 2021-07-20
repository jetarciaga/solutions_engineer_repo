#!/usr/bin/env python3

a = "abcdcba"
b = "noonabbad"
c = 132

def isPalindrome(word:str)->bool:
    """Returns True if given string is palindrome"""

    if not word or word != str(word): # First is we check if the given parameters is a string.
        print("Invalid input!")
        return

    """ Since strings are iterable we will use the indexes to compare
    each letter from start to end. If it encounters a letter which is
    not the same it will return False. There's no need to compare further. """

    for index in range(len(word)):
        if word[index] != word[-(index+1)]: # we used the -(index+1) to traverse in reversed order.
            return False
    print("true // it's written the same forward and backward")
    return True # If the loop end, it means all comparisons are same thus it is palindrome.


isPalindrome(a)
