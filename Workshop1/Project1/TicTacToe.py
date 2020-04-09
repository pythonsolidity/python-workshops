#!/usr/bin/env python
# coding: utf-8

# In[1]:


board = [' _ ' for i in range(0,9)]


# In[2]:


print("The starting board is:")
def printBoard():
    print('')
    print('|     |     |     |')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('|     |     |     |')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('|     |     |     |')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('|     |     |     |')
    print('')

printBoard()


# In[3]:


def check(n):
    if pos%3 == 0:
        win = (board[0] == board[3] == board[6] == sign) or (board[pos] == board[pos+1] == board[pos+2] == sign) or (board[0] == board[4] == board[8] == sign)  or (board[2] == board[4] == board[6] == sign)
    elif pos%3 == 1:
        win = (board[1] == board[4] == board[7] == sign) or (board[pos-1] == board[pos] == board[pos+1] == sign) or (board[0] == board[4] == board[8] == sign)  or (board[2] == board[4] == board[6] == sign)
    else:
        win = (board[2] == board[5] == board[8] == sign) or (board[pos-2] == board[pos-1] == board[pos] == sign) or (board[0] == board[4] == board[8] == sign)  or (board[2] == board[4] == board[6] == sign)
    return win

for i in range(0,9):
    player = i%2
    if player == 0:
        value = int(input("Player 1, please enter an empty position from 0-8: "))
        while board[value] != ' _ ':
            value = int(input("This position is taken, enter an empty position from 0-8: "))
        pos = value
        sign = ' o '
    if player == 1: 
        value = int(input("Player 2, please enter position from 0-8: "))
        while board[value] != ' _ ':
            value = int(input("This position is taken, enter an empty position from 0-8: "))
        pos = value
        sign = ' x '
    board[pos] = sign
    printBoard()
    if check(pos):
        print("Player ", player+1, " wins!")
        break


# In[ ]:




