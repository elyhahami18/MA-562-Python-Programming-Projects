#!/usr/bin/env python
# coding: utf-8

# 
# # Project #3 -- Tkinter Game

## choosing Tic Tac Toe Game
## recieved help via this link: https://www.youtube.com/watch?v=uVrzuKVus7s
## recieved help from https://stackoverflow.com/questions/53580507/disable-enable-button-in-tkinter
# recieved help from https://stackoverflow.com/questions/1529847/how-to-change-the-foreground-or-background-colour-of-a-tkinter-button-on-mac-os
## recieved help via stack overflow link: https://stackoverflow.com/questions/62317055/how-do-i-modify-reset-button-to-make-it-work-correctly

from tkinter import *                      # imports the Tkinter library
from tkinter import messagebox
from tkinter import simpledialog     # simpledialog isn't automatically loaded when you import tkinter
root = Tk()                                # root is what we typically call the base Tk object
root.title('Tic Tac Toe')# This sets the title (look in the upper left hand corner of your window)
root.geometry("400x400")

## Broader gridding below!
def reset_game1():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
## getting the buttons across the first row!
    b1 = Button(root, text = ' ', width = 7, height = 7, foreground = "blue", command =lambda: click(b1))
    b1.grid(column = 0, row = 0)

    b2 = Button(root, text = ' ', width = 7, height = 7, foreground = "blue", command = lambda: click(b2))
    b2.grid(column = 1, row = 0)

    b3 = Button(root, text = ' ', width = 7, height = 7, foreground = "blue", command = lambda: click(b3))
    b3.grid(column = 2, row = 0)

    ## getting the buttons across the second row!
    b4 = Button(root, text = ' ', width = 7, height = 7, foreground = "blue", command = lambda: click(b4))
    b4.grid(column = 0, row = 1)

    b5 = Button(root, text = ' ', width = 7, height = 7, foreground = "blue", command = lambda: click(b5))
    b5.grid(column = 1, row = 1)

    b6 = Button(root, text = ' ', width = 7, height = 7, foreground = "blue", command = lambda: click(b6))
    b6.grid(column = 2, row = 1)

    ## getting the buttons across the third row!

    b7 = Button(root, text = ' ', width = 7, height = 7, foreground = "blue", command = lambda: click(b7))
    b7.grid(column = 0, row = 2)

    b8 = Button(root, text = ' ', width = 7, height = 7, foreground = "blue", command = lambda: click(b8))
    b8.grid(column = 1, row = 2)

    b9 = Button(root, text = ' ', width = 7, height = 7, foreground = "blue", command = lambda: click(b9))
    b9.grid(column = 2, row = 2)
    
clicked = True
count = 0
def click(x):
    global clicked
    global count
    if x['text'] == ' ' and clicked == True:
        x['text'] = 'X'
        clicked = False
        count +=1
        who_won()
    elif x['text'] == ' ' and clicked == False:
        x['text'] = 'O'
        clicked = True
        count +=1
        who_won()
    else:
        messagebox.showerror("Tic Tac Toe", "This box has already selected during this game -- kindly select a different box!")
        
def buttons_disable():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)

 
        
def who_won():
    global winner
    winner = False
    ## check if X's won:
    if b1['text'] == "X" and b2['text'] == 'X' and b3['text'] == "X": ## winning with X's across row 0
        b1.config(highlightbackground='#FFFF00')
        b2.config(highlightbackground='#FFFF00')
        b3.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X's Won!") ## got via notebook 12!
        buttons_disable()
        file_reading_x()
    elif b4['text'] == "X" and b5['text'] == 'X' and b6['text'] == "X": ## winning with X's across row 1
        b4.config(highlightbackground='#FFFF00')
        b5.config(highlightbackground='#FFFF00')
        b6.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X's Won!") 
        buttons_disable()
        file_reading_x()
    elif b7['text'] == "X" and b8['text'] == 'X' and b9['text'] == "X": ## winning with X's across row 2
        b7.config(highlightbackground='#FFFF00')
        b8.config(highlightbackground='#FFFF00')
        b9.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X's Won!") ## got via notebook 12!
        buttons_disable()
        file_reading_x()
    elif b1['text'] == "X" and b4['text'] == 'X' and b7['text'] == "X": ## winning with X's across row 1
        b1.config(highlightbackground='#FFFF00')
        b4.config(highlightbackground='#FFFF00')
        b7.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X's Won!")
        buttons_disable()
        file_reading_x()
    elif b1['text'] == "X" and b4['text'] == 'X' and b7['text'] == "X": ## winning with X's down column 0
        b1.config(highlightbackground='#FFFF00')
        b4.config(highlightbackground='#FFFF00')
        b7.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X's Won!")
        buttons_disable()
        file_reading_x()
    elif b2['text'] == "X" and b5['text'] == 'X' and b8['text'] == "X": ## winning with X's down column 1
        b2.config(highlightbackground='#FFFF00')
        b5.config(highlightbackground='#FFFF00')
        b8.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X's Won!")
        buttons_disable()
        file_reading_x()
    elif b3['text'] == "X" and b6['text'] == 'X' and b9['text'] == "X": ## winning with X's down column 2
        b3.config(highlightbackground='#FFFF00')
        b6.config(highlightbackground='#FFFF00')
        b9.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X's Won!")
        buttons_disable()
        file_reading_x()
    elif b1['text'] == "X" and b5['text'] == 'X' and b9['text'] == "X": ## winning with X's across positively sloped diagonal
        b1.config(highlightbackground='#FFFF00')
        b5.config(highlightbackground='#FFFF00')
        b9.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X's Won!")
        buttons_disable()
        file_reading_x()
    elif b3['text'] == "X" and b5['text'] == 'X' and b7['text'] == "X": ## winning with X's across negatively sloped diagonal
        b3.config(highlightbackground='#FFFF00')
        b5.config(highlightbackground='#FFFF00')
        b7.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X's Won!")
        buttons_disable()
        file_reading_x()
        
#-----------------------------------------------------------------------------------------------------------------------
## check if O's win:
    elif b1['text'] == "O" and b2['text'] == 'O' and b3['text'] == "O": ## winning with X's across row 0
        b1.config(highlightbackground='#FFFF00')
        b2.config(highlightbackground='#FFFF00')
        b3.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O's Won!") ## got via notebook 12!
        buttons_disable()
    elif b4['text'] == "O" and b5['text'] == 'O' and b6['text'] == "O": ## winning with X's across row 1
        b4.config(highlightbackground='#FFFF00')
        b5.config(highlightbackground='#FFFF00')
        b6.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O's Won!") 
        buttons_disable()
    elif b7['text'] == "O" and b8['text'] == 'O' and b9['text'] == "O": ## winning with X's across row 2
        b7.config(highlightbackground='#FFFF00')
        b8.config(highlightbackground='#FFFF00')
        b9.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O's Won!") ## got via notebook 12!
        buttons_disable()
    elif b1['text'] == "O" and b4['text'] == 'O' and b7['text'] == "O": ## winning with X's across row 1
        b1.config(highlightbackground='#FFFF00')
        b4.config(highlightbackground='#FFFF00')
        b7.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O's Won!")
        buttons_disable()
    elif b1['text'] == "O" and b4['text'] == 'O' and b7['text'] == "O": ## winning with X's down column 0
        b1.config(highlightbackground='#FFFF00')
        b4.config(highlightbackground='#FFFF00')
        b7.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O's Won!")
        buttons_disable()
    elif b2['text'] == "O" and b5['text'] == 'O' and b8['text'] == "O": ## winning with X's down column 1
        b2.config(highlightbackground='#FFFF00')
        b5.config(highlightbackground='#FFFF00')
        b8.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O's Won!")
        buttons_disable()
    elif b3['text'] == "O" and b6['text'] == 'O' and b9['text'] == "O": ## winning with X's down column 2
        b3.config(highlightbackground='#FFFF00')
        b6.config(highlightbackground='#FFFF00')
        b9.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O's Won!")
        buttons_disable()
    elif b1['text'] == "O" and b5['text'] == 'O' and b9['text'] == "O": ## winning with X's across positively sloped diagonal
        b1.config(highlightbackground='#FFFF00')
        b5.config(highlightbackground='#FFFF00')
        b9.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O's Won!")
        buttons_disable()
    elif b3['text'] == "O" and b5['text'] == 'O' and b7['text'] == "O": ## winning with X's across negatively sloped diagonal
        b3.config(highlightbackground='#FFFF00')
        b5.config(highlightbackground='#FFFF00')
        b7.config(highlightbackground='#FFFF00')
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O's Won!")
        buttons_disable()
# check for tie!       
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        buttons_disable()


reset_game = Button(text = "Start a new game!", state = DISABLED, font = ("Helvatica", 13), bg = "#ffda30", fg = "#000000", 
               command = reset_game1)
reset_game.grid(row = 3, column = 0, columnspan = 3, sticky = 'nsew')
    

def save_info():
    reset_game.config(state = NORMAL)
    x = entry_x.get()
    o = entry_o.get()
    with open("TTT_Game.txt", "w") as f:
        my_dict = {x: [0,0], o: [0,0]}
        f.writelines(str(my_dict))
    
    
#To do that you have to read in the text file, 
#parse it (which results in a dictionary), 
#add items to the dictionary, convert dictionary to text, write out the text   
def file_reading_x():
    with open("TTT_Game.txt", "w") as q:
        x = entry_x.get()
        o = entry_o.get()
        my_dict = {x: [0,0], o: [0,0]}
        my_dict[x][0] +=1
        my_dict[o][1]+=1
        q.writelines(str(my_dict))
        
    

    
label_x = Label(root, text="Name of player using X's:")
label_o = Label(root, text="Name of player using O's:")

entry_x = Entry(root)
entry_o = Entry(root)

button_save = Button(root, text="Save", command=save_info)

label_x.grid()
label_o.grid()
entry_x.grid()
entry_o.grid()
button_save.grid()


# my_dict = {[]: [], []: [], []: [], []: [], []:[]} ## initialize empty dict 
## for every elif, do func(), where func adds 1 to value for associated key (name)


  

root.mainloop()


# In[ ]:





# In[8]:


with open("TTT_Game.txt", "r") as q:
        inside = q.read()
        y=eval(inside)
        print((y))
        


# In[ ]:





# In[ ]:




