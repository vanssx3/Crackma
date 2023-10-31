import sys
import hashlib
import getopt
import os
import platform
import time
import string



arg = "-b"
os = os.name
password = "p"

def bruteForce(password):
    complete = False
    allChars = (string.ascii_letters + string.digits + string.punctuation)
    crackedPass = ""
    x = 0
    while complete != True:
        crackedPass == allChars[x]
        if crackedPass == password:
            complete = True
        x = x + 0

if arg == ("-help"):
    print("To get started, enter one of the arguments:\n-b To brute force a password (plaintext)\n-m For MD5 decryption\n-b For BCrypt decryption\n-s For SHA-256 decryption\n")
    print("Then follow it up with the password you want decrypted in the right format if it needs to be hashed\n")
    print("Use the argument -help to see this message again!")

if arg == ("-b"):
    bruteForce(password)
    bruteTimeI = time.perf_counter()
    print("Starting brute force attack...")
    print("This may take a while. Be patient or else :3")
    print("If you get bored of waiting press CTRL + C to stop the process")
    bruteTimeF = time.perf_counter()
    print("Brute Force completed in " + str(bruteTimeF - bruteTimeI) + " seconds") 





