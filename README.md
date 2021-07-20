# solutions_engineer_repo

repository for technical exam zigzag careers

Hi my name is Jethro Arciaga and I'll be using this repo
for the coding exam in zigzag careers.


Level 1 palindrome

Time Complexity: 0(n)
Space Complexity: 0(1)

palindrome_level_1.py
isPalindrome function which will return True if the given string is palindrome and False if not.

first we need to make sure that all input that it will accept are strings, if not it should return an invalid input.

since strings are iterable we will use indexes to traverse each letter from index[0] to the end and index[-1] going back to start.

since 0 is the starting index and -1 is the ending index. We will add(+)1 for the index that will traverse backward.

If it encounters an index which is not same value. It will break out of the loop and return False. If it reach the end it means every item is same.


Level 2 palindrome

Time Complexity: 0(n)
Space Complexity: 0(n)

palindrome_level_2.py
longestPalindrome will return the longest possible palindrome. Only one will be returned.

We use try and except block to catch error. If the argument given is not string or empty string it will return Invalid input or no palindrome.

We use dictionary to store characters of the given string that appeared twice.

We created reversed_word to get the negative indexes of the given string.

We loop through the dictionary using its key. The key in the dictionary stores the letter that appeared twice in the given string.

Then, we append the sliced given string to the list we initialized.

Lastly we organized the palindromes list from longest to shortest then we only return the longest palindrome in the list.


Level 3 palindrome

Time Complexity: 0(2^n)
Space Complexity: 0(n)

palindrome_level_3.py

Actually this one is hard for me it really took me a lot of time and research to solve this one. I still can't wrap my head around it. I'll try to explain it as how I understand it.

First we initialize two list the one will store all the possible palindromes and the other one will store the current partition.

Then we create a recursive function. We set the base case that will also help us to avoid error and we created a copy of the "part" list because we don't want to reference from it.

We will use the indexes to slice all possible palindrome but we have to create another function to check if the sliced string is a palindrome and if not it will be ignored.

If it's palindrome we will now append it to the "part" list that we initialized. Then to iterate through all the possible palindrome we now use recursion and use +1 to move to the next iteration.

We also use part.pop() to remove the last item in the list.

We use the depthFirstSearch(0) index 0 because that's the beginning of an index and then it will iterate through by recursion.

Then we get the last resulting palindrome because that contains the longest possible palindrome and the less or optimal cut. Then we get the length then minus (-) 1 to get how many cut the given string have to return all the possible palindromes.

The other function isPali will check if the given value of an index is same. If it's same it will return True and if not False.
