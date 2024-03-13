import tkinter as tk
from tkinter import *
from tkinter import ttk
import random as rnd
from random import *

root = Tk()
root.title("Password Manager")
root.config(padx= 50, pady=50)

#_______________________________________LOGIC____________________________________#


def saving_data():
    data_file = open("DataFile.txt","a+")
    data_file.write(f"""
    Website: {entry_website.get()}
    Email/Username: {entry_user.get()}
    Password: {entry_password.get()}
    """)

def cleaning_data():
    data_file = open("DataFile.txt","w+")
    data_file.close()
def generate_password():



    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)

    password = ''.join(password_list)
    entry_password.insert(0, password)

#_________________________________________UI  SETUP_______________________________#
lock_img = PhotoImage(file= "Image20240309143137.png")
canvas = Canvas(root,width=200,height=200)
canvas.create_image(100,100, image = lock_img )
canvas.grid(row = 0 , column = 1)

#_______________________________________LABELS____________________________________#
text_web = ttk.Label(root, text="Website")
text_web.grid(row = 1, column = 0)

text_user = ttk.Label(root, text="Email/Username")
text_user.grid(row = 2, column = 0)

text_password = ttk.Label(root, text="Password:")
text_password.grid(row =3, column = 0)

#_______________________________________ENTRY____________________________________#
entry_website = ttk.Entry(root,width=35)
entry_website.grid(column = 1,row = 1, columnspan = 2, pady = 5,padx = 2)
entry_website.focus()

entry_user = ttk.Entry(root, width= 35)
entry_user.insert(0,"mrakkus15@gmail.com")
entry_user.grid(column = 1,row = 2, columnspan = 2,pady = 5,padx = 2)

entry_password = ttk.Entry(root, width=21)
entry_password.grid(column = 1,row = 3,pady = 5,padx = 2)

#_______________________________________BUTTONS____________________________________#
button_gen_pass = ttk.Button(root,text="Generate password", command=generate_password)
button_gen_pass.grid(column = 2, row = 3)

button_add = ttk.Button(root,text="Add",width=45,command=saving_data)
button_add.grid(column = 1, row = 4, columnspan = 3)

button_clean_file = ttk.Button(root,text="Clean file",width=20,command=cleaning_data)
button_clean_file.grid(column = 2, row = 5, columnspan = 2)

root.mainloop()