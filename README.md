# Password Manager by DragonFireEx

This is a simple password manager with encryption and a graphical user interface (GUI) built using Python 3.13 and Tkinter. All data is securely stored in an encrypted `data.json` file using a secret key.

## Features

- Add new entries with website, login, and password
- Display all saved entries
- Encrypt and decrypt data using a custom key
- Delete entries by website name
- Refresh data in the GUI
- Validate empty fields and handle errors
- Automatically create `data.json` if it does not exist

## Technologies Used

- Python 3.13
- Tkinter for GUI
- `cryptography.fernet` for encryption
- JSON for data storage
- Standard libraries: `os`, `re`, `tkinter.messagebox`

## How to Run

1. Make sure Python 3.13 is installed on your system.
2. Install the required libraries:
   pip install cryptography

## Security
- All login data is encrypted before being saved.
- The encryption key is required to read the data. Without it, decryption is not possible.
- Do not delete or lose the key unless you no longer need access to the saved data.

## Warning
If you delete the secret encryption key from the project folder, you will lose access to all saved data in data.json during the next application launch. The data will not be recoverable without the original key.
