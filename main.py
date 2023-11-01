import sys # Allows for arguments
import hashlib # Allows for hash algorithms
import time # Allows for making timers
import string # Allows for character library
import itertools # Allows for better iterations

# Change this to change the max length for passwords!
maxChars = 10

# Gets terminal arguments
arg3 = ""
arg1 = sys.argv[1]
if arg1 != ('--help'):
    password = sys.argv[2]
    arg2 = sys.argv[3]
if len(sys.argv) == 5:
    if sys.argv[4] != '-v':
        print("Invalid argument! Run --help for usage info")
        raise SystemExit
    elif sys.argv[4] == '-v':
        arg3 = sys.argv[4]

# Brute Force algorithm
def bruteForce():
    print("Brute Force Attack - trying to crack:", password)
    print("If you want to stop the attack then press CTRL + C")
    time.sleep(3)
    print("Starting Brute Force Attack...")
    time.sleep(0.5)
    startTimeB = time.time()
    allChars = string.printable
    tries = 0
    for length in range(1, maxChars):
        for combination in itertools.product(allChars, repeat=length):
            guess = "".join(combination)
            tries = tries + 1
            if arg2 == '-p':
                guessB = guess
            if arg2 == '-m':
                guessB = hashlib.md5(guess.encode('UTF-8')).hexdigest()
            elif arg2 == '-b':
                guessB = hashlib.BCrypt(guess.encode('UTF-8')).hexdigest()
            elif arg2 == '-s':
                guessB = hashlib.sha256(guess.encode('UTF-8')).hexdigest()
            if arg3 == '-v':
                print(tries, ", ", guess)
            if guess == password:
                endTimeB = time.time()
                print("Password Cracked! Try a more secure password :3")
                print("Your password was: ", guess)
                timeB = (endTimeB - startTimeB)
                print("Cracking took ", timeB, " seconds and ", tries, "tries")
                raise SystemExit

# Dictionary Attack algorithm
def dictionaryAttack():
    print("Dictionary Attack - trying to guess:", password)
    print("If you want to stop the attack then press CTRL + C")
    time.sleep(3)
    print("Starting Dictionary Attack...")
    time.sleep(0.5)
    startTimeD = time.time()
    tries = 0
    with open('passwords.txt','r') as passlist:
        for line in passlist:
            tries = tries + 1
            passwordD = password + "\n"
            if arg2 == '-p':
                lineD = line
            if arg2 == '-m':
                lineD = hashlib.md5(line.encode('UTF-8')).hexdigest()
            if arg2 == '-b':
                lineD = hashlib.BCrypt(line.encode('UTF-8')).hexdigest()
            if arg2 == '-s':
                lineD = hashlib.sha256(line.encode('UTF-8')).hexdigest()
            if arg3 == '-v':
                print(lineD)
            if lineD == passwordD:
                endTimeD = time.time()
                print("Password Guessed! Try a more secure password :3")
                print("Your password was: ",line)
                timeD = (endTimeD - startTimeD)
                print("Guessing took ", timeD, " seconds")
                raise SystemExit
        print("Wow! You have a secure password!")
        print("Unable to guess password - input logged to secure external server") # This is not true, just a funny joke :)
        raise SystemExit


# Checks user inputs to verify if they are valid
# Note that is still possible to passthrough unbrute-forcable hashes if the password
# that the hash decrypts to is > maxChars due to the nature of hashing.
def checker():
    if arg2 != '-p': # Checks if the hash argument is valid
        if arg2 != '-b':
            if arg2 != '-s':
                if arg2 != '-m':
                    print("Invalid Hash Argument! Run --help for usage info")
                    raise SystemExit
    if arg1 == '-b': # Checks if the password is less than or equal to maxChars if brute forcing plaintext
        if arg2 == '-p':
            if len(password) >= maxChars:
                print("Invalid Password - Too many characters! Run --help for usage info")
                raise SystemExit
    if arg2 == '-m': # Checks if the MD5 hash is valid based on expected hash length
        if len(password) != 32:
            print("Incorrect MD5 Hash - Did you enter your hash correctly?")
            raise SystemExit
    if arg2 == '-b': # Checks if the BCrypt hash is valid based on expected hash length
        if len(password) != 64:
            print("Incorrect BCrypt Hash - Did you enter your hash correctly?")
            raise SystemExit
    if arg2 == '-s': # Checks if the SHA-256 hash is valid based on expected hash length
        if len(password) != 64:
            print("Incorrect SHA-256 Hash - Did you enter your hash correctly?")
            raise SystemExit

    

#  Argument calls
if arg1 == ("-b"): # Call for brute force
    checker()
    bruteForce()
elif arg1 == ("-d"): # Call for dictionary attack
    checker()
    dictionaryAttack()
elif arg1 == ("--help"): # Call for usage information
    print("Welcome to passwordCracker!\n")
    print("To get started, run the program with the first argument corresponding to the crack type:")
    print(" -b For a Brute Force Attack")
    print(" -d For a Dictionary Attack\n")
    print("The second argument should be the password you want cracked (Hashed or Plaintext)")
    print("Any password should be no more than " + maxChars.__str__() + " characters when fully decrypted!")
    print("The third argument should correspond to the hash algorithm used:")
    print(" -p For plaintext (No hash algorithm)")
    print(" -m For MD5")
    print(" -b for BCrypt")
    print(" -s for SHA-256\n")
    print("At the end you can optionally add -v to list all guesses (takes SIGNIFICANTLY more time)")
    print("An example call if you wanted to brute force Hi! in plaintext while seeing all guesses:")
    print(" $ python3 main.py -b Hi! -p -v\n")
    print("Use the argument --help to see this message again!")
    raise SystemExit
else: # Shows if argument is invalid
    print("Invalid Argument! Run --help for usage info")
    raise SystemExit
 
