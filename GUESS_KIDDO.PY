import tkinter
from tkinter import *
import random

def set_text(text):
    current_text = entry.get() + text
    entry.delete(0, END)
    entry.insert(0, current_text)

def instruction():
    tkinter.messagebox.showinfo('Welcome To the GUESS KIDDO Game', 
                                'You have 3 attempts to play this game.\n'
                                'There are a few images in this game.\n'
                                'You have to guess them correctly.')

def display_image(image):
    label_image.config(image=image)
    label_image.image = image

turns = 3
def check_answer(entry_value):
    global turns
    correct_answers = {"DOG": Image1, "SQUIRREL": Image2, "HORSE": Image3, 
                       "WOLF": Image4, "ROOSTER": Image5, "FROG": Image6}
    
    if entry_value in correct_answers:
        tkinter.messagebox.showinfo('Answer', 'Congratulations, you got it!')
        if correct_answers[entry_value]:
            display_image(correct_answers[entry_value])
    elif turns > 0:
        turns -= 1
        tkinter.messagebox.showinfo('Answer', f'You are wrong.\nYou have {turns} guesses left.')
    else:
        tkinter.messagebox.showinfo('Remaining Guesses', 'You are out of guesses!')
    
    entry.delete(0, END)

def new_random_word():
    random_image = random.choice(images_list)
    display_image(random_image)

window = Tk()
window.title("GUESS KIDDO")
window.geometry('1080x720')

Image1 = PhotoImage(file="O:\\CODES\\PYTHON\\PROJECTS\\HANGMAN\\ani images\\animated-dog-image-0240.gif")
Image2 = PhotoImage(file="O:\\CODES\\PYTHON\\PROJECTS\\HANGMAN\\ani images\\squirrel.gif")
Image3 = PhotoImage(file="O:\\CODES\\PYTHON\\PROJECTS\\HANGMAN\\ani images\\horse.gif")
Image4 = PhotoImage(file="O:\\CODES\\PYTHON\\PROJECTS\\HANGMAN\\ani images\\wolf.gif")
Image5 = PhotoImage(file="O:\\CODES\\PYTHON\\PROJECTS\\HANGMAN\\ani images\\rooster.gif")
Image6 = PhotoImage(file="O:\\CODES\\PYTHON\\PROJECTS\\HANGMAN\\ani images\\frog.gif")

images_list = [Image1, Image2, Image3, Image4, Image5, Image6]

background = PhotoImage(file="O:\\CODES\\PYTHON\\PROJECTS\\HANGMAN\\ani images\\white.gif")
label_background = Label(window, image=background)
label_background.place(relwidth=1, relheight=1)

frame1 = Frame(window, bg='#0a202b', bd=10)
frame1.place(relx=0.5, rely=0.05, relwidth=0.85, relheight=0.7, anchor='n')

frame3 = Frame(frame1, bg='#0a202b', bd=5)
frame3.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.8, anchor='n')

label_image = Label(frame3)
label_image.place(relwidth=1, relheight=1)
display_image(Image1)

frame2 = Frame(window, bg='#0a202b', bd=10)
frame2.place(relx=0.5, rely=0.8, relwidth=0.85, relheight=0.15, anchor='n')

entry = Entry(frame2, font=40)
entry.place(relwidth=0.6, relheight=1)

title = Label(window, text="Welcome To the Guess Kiddo Game", font=120, bg='white')
title.place(x=0,y=-20,relx=0.5, rely=0.1, relwidth=0.6, relheight=0.05, anchor='n')

Button(frame2, text="OK", font=12, bg='grey', command=lambda: check_answer(entry.get())).place(relx=0.65, relwidth=0.35, relheight=1)

Button(window, text="Click here for instructions", font=100, bg='grey', command=instruction).place(x=-200, y=30, relx=0.5, rely=0.65, relwidth=0.2, relheight=0.05, anchor='n')
Button(window, text="NEW WORD", font=100, bg='grey', command=new_random_word).place(x=200, y=30, relx=0.5, rely=0.65, relwidth=0.2, relheight=0.05, anchor='n')

window.mainloop()
