from tkinter import *
from tkinter import messagebox
from password_generator import Password

PASSWORDS_FILE_PATH = "passwords.txt"
RED_COLOR = "#FF0000"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = Password(4, 2, 2, 4)
    password.generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0, password.generate_password())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def is_website_valid(website):
    if len(website) <= 0:
        return False
    else:
        return True


def is_username_valid(username):
    if len(username) <= 0:
        return False
    else:
        return True


def is_password_valid(password):
    if len(password) <= 0:
        return False
    else:
        return True


def save_password():
    error = False
    website = website_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not is_website_valid(website):
        website_entry.delete(0, END)
        error = True
    if not is_username_valid(username):
        username_entry.delete(0, END)
        error = True
    if not is_password_valid(password):
        password_entry.delete(0, END)
        error = True
    if error:
        messagebox.showerror(title="Values missing error", message="Please fill all fields with valid data")

    else:
        save_approved = messagebox.askyesnocancel(title="Sure to save", message=f"There are the details provided: \n"
                                                  f"Website:  {website}\n"
                                                  f"Username:  {username}\n"
                                                  f"Password:  {password}\n")
        if save_approved:
            with open(PASSWORDS_FILE_PATH, "a") as file:
                file.write(f"| {website} | {username} | {password} |\n")
            clear_values()
    website_entry.focus()


def clear_values():
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

# Logo section
logo_picture = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
logo_picture.create_image(100, 150, image=logo_image)
logo_picture.grid(row=0, column=1, columnspan=2)

# Website input field
Label(text="Website:", justify="left").grid(row=1, column=0)
website_entry = Entry(width=39)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W)
website_entry.focus()

# Email/username input field
Label(text="Email/Username:").grid(row=2, column=0)
username_entry = Entry(width=39)
username_entry.grid(row=2, column=1, columnspan=2, sticky=W)

# Password input
Label(text="Password:").grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=W)
password_entry.get()

# Generate password button
Button(text="Generate Password", command=generate_password).grid(row=3, column=2)

# Add button input
Button(text="Add", width=37, command=save_password).grid(row=4, column=1, columnspan=2, sticky=W)

window.mainloop()
