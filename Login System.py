from tkinter import *
import os
import shutil


def register_user():

    global username_info #for testing delete later 
    global password_info #for testing delete later

    
    username_info = username.get()
    password_info = password.get()

    #os.makedirs(username_info)
    file=open(username_info, "w")#change username_info to change the name of the file that has the username and password
    file.write("Username:\n")
    file.write(username_info +"\n")
    file.write("Password:\n")
    file.write(password_info)
    file.close()
    #shutil.move('dataname', username_info)

    
    
    entry_username.delete(0, END)
    entry_password.delete(0, END)

    Label(screen1, text = "Registration successful!", fg = "green", font =("roboto", 12)).pack()

def destroyed():
    screen4.destroy()

def destroyed1():
    screen5.destroy()
    

def login_completed():
    session()

def saved():
    Label(screen7, text="Saved", fg = "green", font = ("Roboto", 12)).pack()


def save():
    filename_get = filename.get()
    notes_get = notes.get()

    data = open(filename_get, "w")
    data.write(notes_get)
    data.close()

    saved()

def session():
    screen6 = Toplevel(screen)
    screen6.title("Dashboard")
    screen6.geometry("350x250")
    Label(screen6, text = "Welcome to the dashboard").pack()
    Button(screen6, text = "Create secret note", command = create_secret_notes).pack()
    Button(screen6, text = "View secret note", command = view_secret_notes).pack()
    Button(screen6, text = "Delete secret note").pack()

def create_secret_notes():
    global filename
    global notes
    global screen7

    filename = StringVar()
    notes = StringVar()
    
    screen7 = Toplevel(screen)
    screen7.title("Make Notes")
    screen7.geometry("250x150")
    Label(screen7, text = "Enter a filename: ").pack()
    Entry(screen7, textvar = filename).pack()
    Label(screen7, text = "Enter secret notes: ").pack()
    Entry(screen7, textvar = notes).pack()
    Button(screen7, text = "Save", command = save).pack()

def view_secret_notes():

    global filename
    global notes
    global screen8

    filename = StringVar()
    notes = StringVar()
    
    screen8 = Toplevel(screen)
    screen8.title("View Notes")
    screen8.geometry("250x150")

    list_files = os.listdir()
    Label(screen8, text = "Choose one of the filenames").pack()
    Label(screen8, text = all_files).pack()

    
   
def pass_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Retype pass!")
    screen4.geometry("250x150")
    Label(screen4, text = "Password Error!").pack()
    Button(screen4, text = "OK", command = destroyed).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Retype user!")
    screen5.geometry("250x150")
    Label(screen5, text = "User not found!").pack()
    Button(screen5, text = "OK", command = destroyed1).pack()


def login_verify():
    username1 = user_verify.get()
    password1 = pass_verify.get()

    entry_password1.delete(0, END)
    entry_username1.delete(0, END)

    
    list_files = os.listdir() #Make it so it checks inside folder 
    if username1 in list_files:
        file1=open(username1, "r")
        verify = file1.read().splitlines()

        if password1 in verify:
            login_completed()
        else:
            pass_not_recognized()

    else:
        user_not_found()

def register_page():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("350x250")

    global username
    global password
    global entry_username
    global entry_password
    
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter your details").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    entry_username = Entry(screen1, textvariable = username)
    entry_username.pack()
    Label(screen1, text = "Password * ").pack()
    entry_password = Entry(screen1, textvariable = password)
    entry_password.pack()
    Label(screen1, text="").pack()
    entry_password.config(show="*");

   
    password_show = Button(screen1, text="Show password!", height = "1", width = "12", command = buttonshow).pack()
    password_hide = Button(screen1, text="Hide password!", height = "1", width = "12", command = buttonhide).pack()
    Button(screen1, text = "Register", height = "1", width = "10", command = register_user).pack()


def buttonshow():
    entry_password.config(show="");
    
def buttonhide():
    entry_password.config(show="*");

    
def login_page(): 
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("350x250")

    Label(screen2, text = "Please enter your login details").pack()
    Label(screen2, text = "").pack()

    global user_verify
    global pass_verify
    
    user_verify = StringVar()
    pass_verify = StringVar()

    global entry_username1
    global entry_password1
    
    Label(screen2, text = "Username * ").pack()
    entry_username1 = Entry(screen2, textvariable = user_verify)
    entry_username1.pack()
    Label(screen2, text = "Password * ").pack()
    entry_password1 = Entry(screen2, textvariable = pass_verify)
    entry_password1.pack()
    Label(screen2, text = "").pack()
    entry_password1.config(show="*");


    password_show1 = Button(screen2, text="Show password!", height = "1", width = "12", command = buttonshow1).pack()
    password_hide1 = Button(screen2, text="Hide password!", height = "1", width = "12", command = buttonhide1).pack()

    Button(screen2, text = "Login", height = "1", width = "10", command = login_verify).pack()

def buttonshow1():
    entry_password1.config(show="");
    
def buttonhide1():
    entry_password1.config(show="*");

    
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("350x250")
    screen.title("Secret Notes Beta")
    Label(text="Secret Notes Beta", bg = "grey", width = "300", height = "2", font = ("Roboto", 12)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "1", width = "25", font = ("roboto", 12), command = login_page).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "1", width = "25", font = ("roboto", 12), command = register_page).pack()

    screen.mainloop()

main_screen()
