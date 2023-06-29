from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def p():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    input3.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def click():
    website=input1.get()
    email=input2.get()
    password=input3.get()
    if len(website)==0 or len(password)==0:
        messagebox.showerror(title="info",message="Please enter the field")
    else:
        ok = messagebox.askokcancel(title="info",
                                    message=f"Website:{website}\nEmail:{email}\nPassword:{password}\n Is it okay to save?")
        if ok:
            f = open("file.txt", "a")
            L = [website + ' | ', email + ' | ', password + '\n']
            f.writelines(L)
            f.close()
            input1.delete(0, 'end')
            input3.delete(0, 'end')







# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('Password Manger')

window.config(pady=50,padx=50)
canvas=Canvas(width=200,height=200)
myimg = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=myimg)#as width and height is 200
canvas.grid(column=1,row=0)
website=Label(text="Website:")
website.grid(column=0,row=1)
input1=Entry(width=35)
input1.grid(column=1,row=1,columnspan=2)
email=Label(text="Email/username:")
email.grid(column=0,row=2)
input2=Entry(width=35)
input2.grid(column=1,row=2,columnspan=2)
input2.insert(0,"abc.gmail.com")
password=Label(text="Password:")
password.grid(column=0,row=3)
input3=Entry(width=35)
input3.grid(column=1,row=3)
button=Button(text="Generate",command=p)
button.grid(row=3,column=4)
button1=Button(text="Add",width=36,command=click)
button1.grid(row=4,column=1)


window.mainloop()