#!/usr/bin/env python3

a = "noonabbad"
b = "abaxyzzyxf"

def countPalindrome(word:str):
    result = [] # will store all the possible partition
    part = [] # will store the current partition.

    """ We create another function inside a function so that it has access to it's local
    variable and the argument passed on. """

    def depthFirstSearch(i:int): # "i" will be the index of the character we are currently at.
        """ This function will search all the possible palindrome. """

        if i >= len(word): # base case for recursion.
            result.append(part.copy()) # we used .copy() so we don't reference to the part list we initialize.
            return

        """ We will use the indexes to slice all the possible palindromes.
        We will create a separate function to check if the compared word is palindrome.
        If it's palindrome append it to the part list we initialize."""

        for j in range(i, len(word)):
            if isPali(word, i, j):
#                 print(i, j+1)
                part.append(word[i:j+1])
#                 print(part)
                depthFirstSearch(j+1) # recursion to look for additional palindrome.
                part.pop() # for clean up since we only have a single partition variable.
#                 print()

    """ We then get the last item in the list because that's the end of each search.
    Then subtract 1 to the length of the last index to return how many cut it needs to
    return each possible palindrome."""

    depthFirstSearch(0)
    print(str(len(result[-1])-1) + " // " + " | ".join(result[-1]))
#     print(result)
    return len(result[-1])-1


def isPali(word:str,l:int,r:int)->bool:
    """ This function will check if the word is palindrome."""
    while l < r:
        if word[l] != word[r]:
            return False
        l, r = l+1, r-1
    return True


countPalindrome(a)
