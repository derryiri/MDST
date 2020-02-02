"""
MDST Workshop 1 - Python Basics Starter Code
"""
from random import randrange
from base64 import b64encode 
from base64 import b64decode
# Add any imports you need here:


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
   
    
    if(num % 2):
        print("odd!")
    else:
        print("even!")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    rand_num = randrange(1, 9)
    guess = input("Guess: ")
    if(guess != "exit"):
        while(int(guess) != rand_num):
            
            if(int(guess) > rand_num):
                print("Too high")
            else:
                print("Too low")
                
            guess = input("Guess: ")
            
            if(guess == "exit"):
                break
            
            
            
        print("Exactly right")
        
            
       

def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    

    
    if(string[::-1] == string):
        print("True")
    else:
        print("False")


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    encyrpted_user = username.encode("utf-8")
    encrypted_psw = password.encode("utf-8")
    encyrpted_user = b64encode(encyrpted_user)
    encrypted_psw = b64encode(encrypted_psw)
    
    file = open(filename, "w+")
    file.write(str(encyrpted_user))
    file.write("\n")
    file.write(str(encrypted_psw))
    file.write("\n")
    file.close()
    
    
    
def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    
    file = open(filename, "r")
    contents = file.readlines()
    counter = 0;
    
    for i in contents:
        if(counter % 2):
            pre = "Password: "
        else:
            pre = "Username: "
            
        decoded = (i[1:]).encode('ascii')
        msg = b64decode(decoded)
        message = msg.decode('ascii')
        print(pre + message)
        counter += 1
    
    file.close()

    if(password):
        #file = open(filename, "w")
        encrypted_psw = password.encode("utf-8")
        encrypted_psw = b64encode(encrypted_psw)
        
        file = open(filename, 'r')
        user = file.readline()
        file.close()
        new_file = open(filename, 'w')
        new_file.write(user)
        new_file.write(str(encrypted_psw))
      
        new_file.close()


if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
    
