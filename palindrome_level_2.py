#!/usr/bin/env python3

a = "abaxyzzyxf"
b = "noonabbad"

def longestPalindrome(word:str)->str:
    """ Returns a string of longest possible palindrome """

    try:
        """ What I'm thinking is creating a dictionary and storing each letter of the word
        provided in the argument. The letter will be the key and the number of times the
        letter appeared will be the value. """

        palindromes = []
        mapping = {}
        for letter in word:
            if letter not in mapping:
                mapping[letter] = 1
            else:
                mapping[letter] += 1

        """ I'm thinking of removing the item in which the letter appeared only once. Because
        if it only appeared once it means it's either the middle letter of the palindrome or
        it's not included in the longest palindrome. """

        for item in list(mapping):
            if mapping[item] < 2:
                mapping.pop(item)

        """ Creating a reversed word of the given argument will let me check the index number
        of the letter in a reversed order. """

        letters = [letter for letter in word]
        letters.reverse()
        reversed_word = "".join(letters)

        """ We'll use the dictionary to  get the index number of the first and last occurence
        of the letter which appeared multiple times in the provided argument. We use the provided
        argument to get the first occurence and the reversed word of the argument to get the last.
        Then we will slice the palindrome and store it to the list we initialized earlier. """

        for key in mapping.keys():
            palindromes.append(word[word.index(key): -reversed_word.index(key)]) # add (-) to the reversed_word

        print(max(palindromes, key=len))
        return max(palindromes, key=len) # returns the largest

    except ValueError: # This line will catch invalid input.
        return "Invalid input or no palindrome"



longestPalindrome(a)
