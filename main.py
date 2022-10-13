from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from password_generator import Password
import json

PASSWORDS_FILE_PATH = "passwords.json"
RED_COLOR = "#FF0000"


# ---------------------------- SEARCH CREDENTIALS ------------------------------- #
def search_credentials():
    website = website_entry.get().strip()
    if not website:
        messagebox.showerror(message="Please provide website name")
    else:
        try:
            with open(PASSWORDS_FILE_PATH, "r") as file:
                json_data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(message="No any stores were added yet")
        else:
            if website in json_data:
                messagebox.showinfo(message=f"Data for store {website} was found\n"
                                            f"Username: {json_data[website].get('username')}\n"
                                            f"Password: {json_data[website].get('password')}")
            else:
                messagebox.showerror(message=f"There is no data for requested store {website}")

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
        data = {
            website: {
                "username": username,
                "password": password},
        }
        save_to_file(data)
        clear_values()
    website_entry.focus()


def save_to_file(data):
    try:
        with open(PASSWORDS_FILE_PATH, "r") as file:
            json_data = json.load(file)
    except FileNotFoundError:
        with open(PASSWORDS_FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)
    else:
        json_data.update(data)
        with open(PASSWORDS_FILE_PATH, "w") as file:
            json.dump(json_data, file, indent=4)



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
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky=W)
website_entry.focus()

# Search button
search_button = Button(text="Search", width=13, command=search_credentials)
search_button.grid(row=1, column=2)

# Email/username input field
Label(text="Email/Username:").grid(row=2, column=0)
username_entry = Entry(width=39)
username_entry.grid(row=2, column=1, columnspan=2, sticky=W)

# Password input
Label(text="Password:").grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=W)

# Generate password button
Button(text="Generate Password", command=generate_password).grid(row=3, column=2)

# Add button input
Button(text="Add", width=37, command=save_password).grid(row=4, column=1, columnspan=2, sticky=W)

window.mainloop()
#sasd
#adsasd
#asdasdsa