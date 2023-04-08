#!/usr/bin/env python
# coding: utf-8

# 
# # Project #1 -- Bulls and Cows
# ## Bulls and Cows is an old number game played as follows:

# Each of two players selects 4 digits to make up a number.  The number contains no digit repetition.  The number could start with zero, for instance "0539" is a valid choice.  The purpose of the game is to take turns guessing your opponent's number, as follows: Let's pretend that player 1 choice is indeed "0539", then player 2 might try to start the game by guessing "0123". Player 1 must then provide the following feedback: "1 Cow - 1 Bull".  The "cow" corresponds to number 3 that IS in player 1's number, but it is not in the correct position.  The "bull" corresponds to the number zero which was guessed correctly, that is, the correct digit in the right position. Players should write down the corresponding feedback from each guess so that each new guess is based on prior information. The player who guesses its opponent number first wins! 

# In[3]:


# getting numbers from the user and from the computer! 
user_num = input("Select 4 digits to make up a number without digit reptition") ## get 4 dig number from user
from random import sample ## importing so that we can use the built-in function sample()
cpu_num = sample(list(range(10)), 4) 
print(cpu_num)


            
    


# In[ ]:


## getting user number and cpu number
from random import sample ## importing so that we can use the built-in function sample()
cpu_num = sample(list(range(10)), 4) 
print(cpu_num)

    
## got number of bulls -- that is, correct digit in correct position
def bulls (user_num, cpu_num):
    num_bulls = 0
    for i in range(0,4): ## use for loop
        # now use conditionals to efficiently select outcomes
        if int(user_num[i]) == cpu_num[i]: ## checking to see if the user number is in the correct position in the cpu number (ie. the definition of a bull)
            num_bulls += 1
    return num_bulls
            
## function to get the number of cows -- that is, correct digit in incorrect position
def cows(user_num, cpu_num):
    num_cows = 0
    for i in range(0,4):
        if int(user_num[i]) in (cpu_num) and int(user_num[i]) != cpu_num[i]: ## checking conditions that the 
            # index in the user number is in the cpu number but is not in the correct index (ie. the definition of a cow)
            num_cows +=1
    return num_cows

count = 0 ## set a counter at 0
while True: ## create a while loop
    count +=1
    user_num = input("Select 4 digits to make up a number without digit reptition") ## get 4 dig number from user
    while len(set(user_num)) != 4 or len(user_num)!=4: # considering the edge case of repeating digits and length of user number not being 4 (ie. if user inputs a number too long or too short!)
# note that I recieved help with the set function from the following source:https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
## essentially, the set function first checks if the user's input has any repeating digits by converting the input 
#to a set and then checking the length of the set. If the length is not 4, the function prints an an invalid entry and prompts the user to enter a new number. 
#Otherwise, the function proceeds to count the number of bulls and cows and continue the game as usual.
        user_num = input("Invalid entry. Please enter FOUR DIFFERENT DIGITS. Try again!")
    if bulls(user_num, cpu_num) == 4: # use conditions to effectively select outcomes
        print(f' You won in {count} valid tries!')
        break ## use break for added control
    print(f' Valid entry! Cows: {cows(user_num, cpu_num)} - Bulls: {bulls(user_num, cpu_num)}.') # otherwise, print the number of bulls and cows and continue the game using an f string!


# In[ ]:





# ## The Project
# 
# The task for this project is to write some code to play this game against the computer.  Computer picks number, and user enters guesses based on computer's feedback. This task is only a one-way game, that is the user (you) tries to guess the computer's chosen number, the computer does NOT guess at your number. That task is much more complex!

# ## Notes:
# 
# - You may want to use the built-in function sample(num_list, n ). It selects n different elements from list num_list. It requires the import: "from random import sample".
# <p>
#     
# - For beginners, do NOT worry about validating user's input.  When you get your program to work assuming proper input, THEN you may want to start thinking about checking the input to make your code more robust.
# <p>
# - Given the repetitive nature of the game, you should definitely use functions in your code.
# <p>
# - Pay attention to the standards in your grade file.  This is your very first opportunity to demonstrate that you have aquired the various primary and secondary skills reflected in those standards, so try to incorporate as much of that as possible.
# <p>
# 5. The following is a snap-shot of the output of a version of the game written by Mr. Bayona. Important: The first line "selection is : [2, 3, 7, 6]"
# is there only for demonstration purposes, to compare the user's input with the computer's selection as an example. Obviously printing that line is considered "cheating'...
#     
# ![image.png](attachment:image.png)

# ### If you finish early... some options to continue working on the project:
# 
# - Give the player the option of choosing how many digits they want in the number! <p>
# 
# - Try to write code that allows the computer to try and guess your number. If you don't care how many attempts you make, you can pretty easily do it with a loop.  But try to think through a more systematic approach.
# 
# 

# In[ ]:




