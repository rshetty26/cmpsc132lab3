# Lab 3
This program contains multiple functions. The is_palindrome function checks whether or not a string is a palindrome. It ignores any capitalizations.

The replace function takes a list and replaces every occurance of a said value with a new given value.

The JUMP game consists of a board of size n represented as a Python list that contains only positive numbers, apart from the first element in the list that is always 0 . The integers represent the cost to enter that cell. Starting always from the first element, the goal of the game is to move from the first element to the last with the lowest cost and there are only two kinds of moves: 1) move to the adjacent cell or 2) jump over the adjacent cell to land 2 cells away. For example: 

0 -> 9 -> 5 -> 23 -> 25 -> 13 -> 17 -> 4 -> 12 -> 3

In this board, there are multiple ways to get to the end. Starting always at 0 , our cost so far is 0 . We could then jump to 5 , then jump to 25 , then jump to 17 , then move to 4 and finally jump to 3 for a total cost of 54 . However, if we jump to 5 , move to 23 , jump to 13 , jump to 4 and finally jump to 3 we get a lower cost of 48 . The play_jump function implements this game assuming the board is at most size 15.

The neightbor function takes a positive integer n and a default argument prev and returns the number of digits in n that have the same digit to its left or to its right. 
