from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().title()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please fill all the information")
    else:
        try:
            with open("data.json", 'r') as data_file:
                # read a file
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                # write a file
                json.dump(new_data, data_file, indent=4)
        else:
            # update elements in file
            data.update(new_data)
            with open("data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json", 'r') as data_file:
            web = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found")
    else:
        if website in web:
            messagebox.showinfo(title=website, message=f"Email: {web[website]['email']} \n"
                                                       f"Password: {web[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists")

            # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# website row
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

# Email/username row
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=53)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "manyakhare86@gmail.com")

# Password row
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

generate_pass_button = Button(text="Generate password", command=generate_password)
generate_pass_button.grid(column=2, row=3)

# Add row
add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
