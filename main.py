import sys
import hashlib
import getopt
import time
import string
import itertools


arg = "-b"
password = ""

def bruteForce():
    startTimeB = time.time()
    allChars = string.printable
    for length in range(1, 10):
        for combination in itertools.product(allChars, repeat=length):
            guess = "".join(combination)
            print(guess)
            if guess == password:
                endTimeB = time.time()
                print("Password Cracked! Try a more secure password :3")
                print("Your password was: ", guess)
                timeB = (endTimeB - startTimeB)
                print("Cracking took ", timeB, " seconds")
                raise SystemExit


def dictionaryAttack():
    startTimeD = time.time()
    listLines = 0
    with open('passwords.txt','r') as passlist:
        count = 0
        for line in passlist:
            count += 1
    listLines = count

    


if arg == ("-b"):
    bruteForce()

if arg == ("-help"):
    print("To get started, enter one of the arguments:\n-b To brute force a password (10 characters max for plaintext)\n-g To guess a plaintext password\n-m For MD5 hash decryption\n-b For BCrypt hash decryption\n-s For SHA-256 hash decryption\n")
    print("Then follow it up with the password you want decrypted (Hashed or Plaintext)\n")
    print("Use the argument -help to see this message again!")
 





