from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    random_password = "".join(password_list)

    password_input.insert(0, random_password)

    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == "":
        messagebox.showerror(title="Error", message="You forgot to enter the website.. !!")
    elif email == "":
        messagebox.showerror(title="Error", message="You forgot to enter the email or username.. !!")
    elif password == "":
        messagebox.showerror(title="Error", message="You forgot to enter the password.. !!")
    else:
        is_yes = messagebox.askyesno(title=website, message=f"Email: {email}\nPassword: {password}\n"
                                                            f"\n Do you want to save this data?")
        if is_yes:
            with open("password_data.txt", "a") as password_data:
                password_data.write(f"{website} | {email} | {password}\n")

            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200, highlightthickness=0)

logo = PhotoImage(file="original_logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
website_label.config(pady=15)

website_input = Entry(width=45)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

email_input = Entry(width=45)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "aarsh@gmail.com")

password_label = Label(text="Password")
password_label.grid(column=0, row=3)
password_label.config(pady=15)

password_input = Entry(width=25)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
