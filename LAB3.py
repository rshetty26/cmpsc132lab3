# LAB 3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# All functions should NOT contain any for/while loops or global variables. Use recursion, otherwise no credit will be given

def is_palindrome(txt):
    """
        >>> is_palindrome('noon')
        True
        >>> is_palindrome('tacoCAT')
        True
        >>> is_palindrome('cmpsc132')
        False
        >>> is_palindrome('Level')
        True
    """
        ## YOUR CODE STARTS HERE
    txt = txt.lower()
    if (len(txt) == 2 or len(txt) == 3) and txt[0] == txt[-1]:
        return True
    elif txt[0] == txt[-1]:
        return is_palindrome(txt[1:-1])
    else:
        return False
    pass



def replace(aList, old, new):
    """
        >>> input_list = [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace(input_list, 1, 99.9)
        [99.9, 7, 5.6, 3, 2, 4, 99.9, 9]
        >>> input_list
        [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 5.6, 777) 
        [1, 7, 777, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 8, 99)    
        [1, 7, 5.6, 3, 2, 4, 1, 9]
    """
    ## YOUR CODE STARTS HERE
    if len(aList) == 1:
        if aList[0] == old:
            return [new]
        else:
            return [aList[0]]
    if aList[0] == old:
        return [new] + replace(aList[1:], old, new)
    else:
       return [aList[0]] + replace(aList[1:], old, new)
    pass



def play_jump(board):
    """
        >>> play_jump([0, 9, 5, 23, 25, 13, 17, 4, 12, 3])
        48
        >>> play_jump([0, 48, 31, 85, 25, 21, 4, 46, 55])
        115
        >>> play_jump([0, 10, 13, 16, 4, 11, 16, 6, 14, 6])
        40
        >>> play_jump([0, 48, 31, 85, 25, 21, 4, 46, 54, 12, 42])
        156
    """
    ## YOUR CODE STARTS HERE
    if len(board) <= 1:
        return board[0]
    if len(board) == 2:
        return board[0] + board[1]
    if play_jump(board[1:]) < play_jump(board[2:]):
        return board[0] + play_jump(board[1:])
    else:
        return board[0] + play_jump(board[2:])
    pass



def neighbor(n, prev=-1):
    """
        >>> neighbor(777)
        3
        >>> neighbor(46970)
        0
        >>> neighbor(411477) 
        4
        >>> neighbor(7951452114587444436999) 
        9
        >>> neighbor(22222222222222233)      
        17
    """
    ## YOUR CODE STARTS HERE
    if n < 10: 
        if n == prev:
            return 1
        else:
            return 0
    if (prev == n % 10) or (((n // 10) % 10) == (n % 10)):
        return neighbor(n//10, n % 10) + 1
    else:
        return neighbor(n//10, n % 10)
    pass

if __name__=='__main__':
    import doctest
    doctest.testmod()