from tkinter import *
import math
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    input_pas.insert(0, password)
    pyperclip.copy(password)

    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():
    website = input_website.get()
    email = input_email.get()
    password = input_pas.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="I see some empty fields")
    is_ok = messagebox.askokcancel(title=website, message=f"You want to add: \nEmail: {email} \nPassword: {password} \nDo you want too save?")

    if is_ok:
        f = open("data.txt", "a")
        f.write(f"{website} | {email} | {password}\n")
        input_website.delete(0, END)
        input_pas.delete(0, END)
        f.close()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50, bg="#FFFFFF")

canvas = Canvas(width=200, height=200, bg="#FFFFFF", highlightthickness=0)
background = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", bg="#FFFFFF", fg="#000000")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:", bg="#FFFFFF", fg="#000000")
label_email.grid(column=0, row=2)

label_pas = Label(text="Password:", bg="#FFFFFF", fg="#000000")
label_pas.grid(column=0, row=3)

input_website = Entry(bg="#FFFFFF", fg="#000000", width=35)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_email = Entry(bg="#FFFFFF", fg="#000000", width=35)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, "your@mail.com")

input_pas = Entry(bg="#FFFFFF", fg="#000000", width=21)
input_pas.grid(column=1, row=3)

button_generate = Button(text="Generate password", width=10, command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", command=save_to_file)
button_add.grid(column=1, row=4, columnspan=2)


window.mainloop()