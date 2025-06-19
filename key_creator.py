from cryptography.fernet import Fernet
import os
import json

#if the key is generated the data is open to operations, if the key would be deleted the data will be lost

if not os.path.exists("data.json"):
    with open("data.json", "w") as file:
        json.dump({}, file)

def clear_data_file(filename):
    with open(filename, "w") as file:
        json.dump({}, file, indent=4)
    print(f"No key found! '{filename}' the data file has been cleared.")
    

def check_secret_key():
    k_file = "secret.key"
    if os.path.exists(k_file):
        print("Key found!")
    else:
        clear_data_file("data.json")
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        print("Created new Key!")