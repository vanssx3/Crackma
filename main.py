import sys # Allows for arguments
import hashlib # Allows for hash algorithms
import time # Allows for making timers
import string # Allows for character library
import itertools # Allows for better iterations

# print(sys.argv) for testing agrs

# Gets terminal arguments

arg1 = sys.argv[1]
if arg1 != ('--help'):
    password = sys.argv[2]
    arg2 = sys.argv[3]
if len(sys.argv) == 3:
    arg3 = sys.argv[4]

# Brute Force algorithm
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
            if arg2 == '-m':
                guess = hashlib.md5(guess.encode('UTF-8')).hexdigest()
            if arg2 == '-b':
                guess = hashlib.BCrypt(guess.encode('UTF-8')).hexdigest()
            if arg2 == '-s':
                guess = hashlib.sha256(guess.encode('UTF-8')).hexdigest()
            if arg3 == '-v':
                print(guess, " ", tries)
            if guess == password:
                endTimeB = time.time()
                print("Password Cracked! Try a more secure password :3")
                print("Your password was: ", guess)
                timeB = (endTimeB - startTimeB)
                print("Cracking took ", timeB, " seconds and ", tries, "tries")
                raise SystemExit

# Dictionary Attack algorithm
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
        print("Unable to guess password - input logged to secure external server")
        raise SystemExit

    

#  Argument calls
if arg1 == ("-b"):
    bruteForce()

if arg1 == ("-d"):
    dictionaryAttack()

if arg1 == ("--help"):
    print("Welcome to passwordCracker!\n")
    print("To get started, run the program with the first argument corresponding to the crack type:")
    print(" -b For a Brute Force Attack")
    print(" -d For a Dictionary Attack\n")
    print("The second argument should be the password you want cracked (Hashed or Plaintext)\n")
    print("The third argument should correspond to the hash algorithm used:")
    print(" -p For plaintext (No hash algorithm)")
    print(" -m For MD5")
    print(" -b for BCrypt")
    print(" -s for SHA-256\n")
    print("An example call if you wanted to brute force Hi! in plaintext:")
    print(" $ python3 main.py -b Hi! -p\n")
    print("Use the argument --help to see this message again!")
 





