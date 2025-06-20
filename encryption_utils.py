import json
import os
from cryptography.fernet import Fernet
from tkinter import messagebox

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()


#the key and encrypting object
key = load_key()
fernet = Fernet(key)


def encrypt(text: str, fernet: Fernet) -> str:
    return fernet.encrypt(text.encode()).decode()

def decrypt(token: str, fernet: Fernet) -> str:
    return fernet.decrypt(token.encode()).decode()




data_file = "data.json"

def delete_data_by_name(name):
    if not os.path.exists(data_file):
        print("Error", "Data file does not exist.")
        return

    try:
        with open(data_file, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Error", "Data file is corrupted or empty.")
        return

    if name in data:
        del data[name]
        with open(data_file, "w") as file:
            json.dump(data, file, indent=4)
        print("Success", f"Entry for '{name}' deleted.")
    else:
        print("Error", f"No entry found for '{name}'.")

def show_all_data(text_widget):  # przyjmujemy widget jako argument
    if not os.path.exists(data_file):
        text_widget.insert("end", f"File '{data_file}' no exist.\n")
        return

    try:
        with open(data_file, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        text_widget.insert("end", f"File '{data_file}' is empty or damaged. Try adding some data.\n")
        return

    if not data:
        text_widget.insert("end", "No data to display.\n")
        return
    else:
        text_widget.insert("end", "All data:\n")
        for website_name, credentials in data.items():
            text_widget.insert("end", f"Website name: {website_name}\n")
            text_widget.insert("end", f"Login: {decrypt(credentials.get('login'), fernet)}\n")
            text_widget.insert("end", f"Password: {decrypt(credentials.get('password'), fernet)}\n\n")

            print(f"Website name: {website_name}")
            print(f"Login: {decrypt(credentials.get('login'), fernet)}")
            print(f"Password: {decrypt(credentials.get('password'), fernet)}\n")



def save_data(name,login,password): #this function is getting all the data from user - 1 record of login to website and saving it to data.json

    record = {
        "website-name" : f"{name}",
        "login" : f"{login}",
        "password" : f"{password}"
    }
    #checking if the file exists
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError: #exception handling
                data = {}
    else:
        data = {}


    #encrypting the password and login
    encrypted_login = encrypt(record["login"], fernet)
    encrypted_password = encrypt(record["password"], fernet)

    if record["website-name"] in data:
        print(f"There's already data to this website '{name}'. Do you want to replace it with new one?")
        check = messagebox.askyesno("Confirmation", f"There's already data to this website '{name}'. Do you want to replace it with new one?")
        if check:
            #if website-name is equal to existing one it raplaces it with new data
            data[record["website-name"]] = {
                "login": encrypted_login,
                "password": encrypted_password
            }

            with open(data_file, "w") as file:
                json.dump(data, file, indent=4)
            
            print("Data Saved!")
        else:
            print("Canceled operation.")
    else:
        data[record["website-name"]] = {
                "login": encrypted_login,
                "password": encrypted_password
            }

        with open(data_file, "w") as file:
            json.dump(data, file, indent=4)
            
        print("Data Saved!")