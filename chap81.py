from graphics import *
import random

#accepts a list of words (as a parameter) and a new word (typed in by the user).
#   If the new word
#   starts with a vowel we will add it to our list
def practice (words):
    word = input("Enter a word that starts with a vowel: ")
    while not(word[0].lower() in "aeiou"):
        print("Your word must start with a vowel")
        word = input("Word: ")
    words.append(word)
    
def testPractice():
    wordList = ["apple", "orange", "ant", "elephant"]
    print(wordList)
    practice(wordList)
    print(wordList)

    print()
    practice(wordList)
    print(wordList)

    #print("hi")  - void function

    print()
    practice(wordList)
    print(wordList)
    #call practice

    
#Purpose: Ask user to enter a number greater than 10
#  Function returns the first number entered matching
#     the requirement

##stop: num > 10
##continue: not stop -- not num > 10 => num <= 10


def goodInput():
    msg = "Enter a number greater than 10: "
    num = float(input(msg))
    #while not num > 10:
    while num <= 10:
        print("In loop:", msg)
        num = float(input("Number: "))
    return num
    
#Purpose: Ask user to enter a number 100 or less
#  Function returns the first number entered matching
#     the requirement

#stop: num <= 100

def goodInput2():
    msg = "Enter a number 100 or less: "
    num = float(input(msg))
    #while not num <= 100:
    while num > 100:
        print("In loop:", msg)
        num = float(input("Number: "))
    return num       

    
#Purpose: Ask user to enter a number inclusively between
#    10 and 100 
#  Function returns the first number entered matching
#     the requirement

#stop: num >= 10 and num <= 100
#continue: not stop --> not(num >= 10 and num <= 100)
def goodInput3():
    msg = "Enter a number between 10 and 100: "
    num = float(input(msg))
##    while not(num >= 10 and num <= 100):
    while num < 10 or num > 100:
        print("In loop:", msg)
        num = float(input("Number: "))
    return num      

#Purpose: Ask user to enter a number 20s or 10
#  Function returns the first number entered matching
#     the requirement

##stop: num >= 20 and num < 30 or num == 10
##continue: not (num >= 20 and num < 30 or num == 10)
##      ==> 
   
def goodInput4():
    msg = "Enter a number in 20's or the number 10: "
    num = float(input(msg))
##    while not (num >= 20 and num < 30 or num == 10):
    while (num < 20 or num >= 30) and num != 10: 
        print("In loop:", msg)
        num = float(input("Number: "))
    return num

#Purpose: Ask user to enter a number in the 100s or even
#  Function returns the first number entered matching
#     the requirement

##stop: num >= 100 and num < 200 or num%2 == 0

def goodInput5():
    msg = "Enter a number in 100's or an even number: "
    num = float(input(msg))
    while (num < 100 or num >= 200) and num%2 != 0:
##    while num < 100 or num >= 200 and num%2 != 0:#incorrect
        print("In loop:", msg)
        num = float(input("Number: "))
    return num

def testGoodInput():
##    #example - execute a return function
##    name = input("Enter your name: ")
##    print(name)
    num = goodInput5()  
    print("You entered:", num)


    
#Input: Parameter-None; From user - string representing password
#Output: Return - Boolean
#Purpose: Returns True once user enters correct password - unlimited tries
   # the correct password is "abc"

##   stop: pswd == "abc"
   
def isCorrectPWD():
    msg = "Enter password: "
    pswd = input(msg)
    while pswd != "abc":
        print("Incorrect password.")
        pswd = input(msg)
    return True
    
#Input: From user, string password
#Output: Returns Boolean - True if they entered their pwd in 3 tries;
    #False - otherwise
#Purpose: Ask user to enter their password ('abc')
#  allow user 3 chances to enter it correctly

##stop: numTries >= 3 or pswd == "abc"

def isCorrectPWD2():
    msg = "Enter password: "
    pswd = input(msg)
    numTries = 1
    while numTries < 3 and pswd != "abc":
        print("Incorrect password.")
        pswd = input(msg)
        numTries += 1
    return pswd == "abc" #equivalent to below
##    if pswd == "abc":
##        return True
##    else:
##        return False
    
def testGetPassword():
    if not(isCorrectPWD2()):
        print("You've been locked out of your account.")
    else:
        print("Log-in complete!")


#Input: Parameter - list of numbers
#Output: Return - int
#Purpose: Returns the position of the first number in the list that is
#  20 or higher;  returns -1 if no such number exists in the list
def findBig(nums):
    i = 0
    while nums[i] < 20 and i < len(nums):
        i += 1
    if i == len(nums):
        i = -1
    return i

def testBig():
    values = [15, 10, 13, 20, 14, 40, 2]
    pos = findBig(values)
    print(f"{values}\n{values[pos]} found at {pos}")

    values = [150, 10, 13, 20, 14, 40, 2]
    pos = findBig(values)
    print(f"{values}\n{values[pos]} found at {pos}")

    values = [15, 10, 13, 10, 14, 4, 25]
    pos = findBig(values)
    print(f"{values}\n{values[pos]} found at {pos}")

    values = [15, 10, 13, 9, 14, 0, 2]
    pos = findBig(values)
    print(values)
    if pos == -1:
        print("Big value not in list")
    else:
        print(f"{values[pos]} found at {pos}")

#Input: Terminal - numbers
#Output: return a list
# Purpose: allow user to enter numbers into a list - until
#    user enters a non-positive or a number greater
#    than 100
#     returns the list of "valid" numbers
def getNumbers():

    nums = []
    msg = "Enter number <negative or greater 100 to quit>: "
    num = eval(input(msg))
    

def testGetNumbers():
    values = getNumbers()
    print(values)

#      
#Input: Parameter - None - Terminal: password
#Output: return the valid password
#Purpose: To have user enter a valid password
#  valid pwd - starts with upper case letter or ends with "_"
def setPassword():
    return



def main():
##    #while non-negative numbers  - "clap"
##    num = random.randint(-5, 30)
##    while num >= 0:
##        print("Num: " + str(num) + "\tClap!")
##        num = random.randint(-5, 30)
##        time.sleep(.5)        
##
##    print("The negative numb was: " + str(num))
##
##    #while loop can work like a for loop
##    for i in range(5):
##        print(i)
##    print("After for loop i is: " + str(i))
##    print()
##    
##    i = 0
##    while i < 5:
##        print(i)
##        i += 1
##    print("After...i: " + str(i))
##    print()
##
##    i = 0
##    while i < 5:
##        i += 1
##        print(i)
##    print("After...i: " + str(i))
##
####    #infinite loop
##    print()
##    i = 0
##    while i < 5:
##        i -= 1
##        print(i)
##    print("After...i: " + str(i))
##    
    print()
    i = 2
    while i < 16:
        print(i)
        i += 2
    print("After...i: " + str(i))

    print()
    i = 0
    while i < 14:
        i += 2
        print(i) 
    print("After...i: " + str(i))

    #People usually say reason for stopping -- DeMorgan's Laws
    #eq = equivalent
##    not x > 5 eq x <= 5
##    not x >= 5 eq x < 5
##    not x < 5 eq x >= 5
##    not x <= 5 eq x > 5
##    not x == 5 eq x != 5
##    not x != 5 eq x == 5

    ##    total = 0
##    msg = "Enter a number (negative or 100 to quit): "
##    num = eval(input(msg))
##
##    while num >= 0 and num != 100:
##        total += num
##        num = eval(input(msg))
##
##    print("Total:", total)
