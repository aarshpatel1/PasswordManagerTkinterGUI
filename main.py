from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200, highlightthickness=0)

logo = PhotoImage(file="original_logo.png")
canvas.create_image(100, 100, image=logo)
canvas.pack()

window.mainloop()
