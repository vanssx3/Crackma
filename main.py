import sys
import hashlib
import getopt
import time
import string
import itertools


arg = "-d"
password = "vo30qb"

def bruteForce():
    print("Brute Force Attack: trying to crack ", password)
    print("If you want to stop the attack then press CTRL + C")
    time.sleep(3)
    print("Starting Brute Force attack...")
    time.sleep(0.5)
    startTimeB = time.time()
    allChars = string.printable
    tries = 0
    for length in range(1, 10):
        for combination in itertools.product(allChars, repeat=length):
            guess = "".join(combination)
            tries = tries + 1
            print(guess, " ", tries)
            if guess == password:
                endTimeB = time.time()
                print("Password Cracked! Try a more secure password :3")
                print("Your password was: ", guess)
                timeB = (endTimeB - startTimeB)
                print("Cracking took ", timeB, " seconds and ", tries, "tries")
                raise SystemExit


def dictionaryAttack():
    print("lol dictionary attack")
    startTimeD = time.time()
    tries = 0
    with open('passwords.txt','r') as passlist:
        for line in passlist:
            tries = tries + 1
            passwordD = password + "\n"
            print(line)
            if line == passwordD:
                endTimeD = time.time()
                print("Password Guessed! Try a more secure password :3")
                print("Your password was: ",line)
                timeD = (endTimeD - startTimeD)
                print("Guessing took ", timeD, " seconds")
                raise SystemExit
        print("Wow! You have a secure password!")
        raise SystemExit

    


if arg == ("-b"):
    bruteForce()

if arg == ("-d"):
    dictionaryAttack()

if arg == ("-help"):
    print("To get started, enter one of the arguments:\n-b To brute force a password (10 characters max for plaintext)\n-d To guess a plaintext password\n-m For MD5 hash decryption\n-b For BCrypt hash decryption\n-s For SHA-256 hash decryption\n")
    print("Then follow it up with the password you want decrypted (Hashed or Plaintext)\n")
    print("Use the argument -help to see this message again!")
 





