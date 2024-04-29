from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
  pass
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

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

email_input = Entry(width=45)
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)
password_label.config(pady=15)

password_input = Entry(width=25)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
