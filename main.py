from key_creator import check_secret_key
check_secret_key()#run firstly - checks the key


from encryption_utils import save_data, show_all_data, delete_data_by_name

# save_data("facebook", "user2fb@wp.pl", "fbpass123!")
# save_data("youtube", "user1yt@gmail.com", "ytpass123!")
# show_all_data()



import tkinter as tk
from tkinter import messagebox
import re
from tkinter import simpledialog


#that's the main window
root = tk.Tk()
root.title("Password Manager by DragonFireEx | Decryption & Encryption by your key")
root.geometry("600x400")
root.resizable(False, False)

#helpers
def remove_all_whitespace(text: str) -> str:
    return re.sub(r"\s+", "", text)

#functions to tkinter
def show_data():
    text_output.config(state="normal")
    text_output.delete("1.0", "end")
    show_all_data(text_output)
    text_output.config(state="disabled")

def send_data():
    site = entry_site.get()
    login = entry_login.get()
    password = entry_password.get()
    remove_all_whitespace(site)
    remove_all_whitespace(login)
    remove_all_whitespace(password)
    if site=="" or login=="" or password=="":
        print("Empty fields!")
        messagebox.showerror("Error", "Empty fields!")
        pass
    else:
        save_data(site,login,password)
        show_data()

def delete_data():
    name = simpledialog.askstring("Delete Entry", "Enter the website name to delete:")
    remove_all_whitespace(name)
    if name=="":
        print("Empty fields!")
        messagebox.showerror("Error", "Empty fields!")
        pass
    else:
        delete_data_by_name(name)
        show_data()


#window for inputs
frame_input = tk.LabelFrame(root, text="New data set", padx=10, pady=10)
frame_input.pack(fill="both", expand=True, padx=10, pady=10)

#inputs
label_site = tk.Label(frame_input, text="Website Name:")
label_site.grid(row=0, column=0, sticky="e")
entry_site = tk.Entry(frame_input, width=40)
entry_site.grid(row=0, column=1, padx=5, pady=5)

label_login = tk.Label(frame_input, text="Login:")
label_login.grid(row=1, column=0, sticky="e")
entry_login = tk.Entry(frame_input, width=40)
entry_login.grid(row=1, column=1, padx=5, pady=5)

label_password = tk.Label(frame_input, text="Password:")
label_password.grid(row=2, column=0, sticky="e")
entry_password = tk.Entry(frame_input, width=40)
entry_password.grid(row=2, column=1, padx=5, pady=5)

#window for buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(fill="x", padx=10, pady=(0, 10))
for i in range(3):
    frame_buttons.columnconfigure(i, weight=1)

#buttons
button_save = tk.Button(frame_buttons, text="Save Data Set", command=send_data)
button_save.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

button_refresh = tk.Button(frame_buttons, text="Refresh", command=show_data)
button_refresh.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

button_delete = tk.Button(frame_buttons, text="Delete Data by name", command=delete_data)
button_delete.grid(row=0, column=2, padx=5, pady=5, sticky="ew")



#window to display all the data
frame_display = tk.LabelFrame(root, text="Saved Passwords", padx=10, pady=10)
frame_display.pack(fill="both", expand=True, padx=10, pady=(0,10))

text_output = tk.Text(frame_display, height=8, wrap="word", state="disabled")
text_output.pack(fill="both", expand=True)

root.mainloop()