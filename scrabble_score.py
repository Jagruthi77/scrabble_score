import signal #importing package for timer
import os #importing package for system

global length #declaring length variable as global
dict = ['apple', 'ball', 'cat', 'do','cabbage'] #delcaring dictionary
# Initialising the values for letters in a dictionary{key:value}
score = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2, 
         "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3, 
         "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1, 
         "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4, 
         "X": 8, "Z": 10}


def scrabble_score(word): #Returns the scrabble score for a given word
    points = 0 #Intialising points variable to zero 
    for letter in word.upper(): # looping through the word to calculate score and converting alphabets to upper 
        points += score[letter] # adding up the value for each alphabet and storing in points
    return points # returing the points variable containing scrabblescore

TIMEOUT = 15 # number of seconds your want for timeout

def interrupted(signum, frame): #called when read times out
    print ('Program timedout, please re-execute!!') #printing message for user
    os._exit(os.EX_OK) #To exit from console once timer reaches threshold 15 secs

#Method for timeout alarm
signal.signal(signal.SIGALRM, interrupted)


def main(): #main definition
    signal.alarm(TIMEOUT) 
    print ('You have 15 seconds to type in your word..')#printing message on console to user
    length=int(raw_input("Please enter the length of word: ")) #prompting the user to enter length of word 
    signal.alarm(0)
    signal.alarm(TIMEOUT)
    word = raw_input("Enter a word: ") # Prompting the user for word input 
    signal.alarm(0)
    if word.isalpha():# checking if the characters are alphabets or not 
        if length == len(word): #checking the length entered by user and length of word
            result=scrabble_score(word) # catching the result from scrabble_score method
            if word.lower() in dict: # checking the word in dictionary
                print("The scrabble score of", word, "is", result) # printing the message on console
            else: # else condition executed when if condition fails 
                print("Entered word should exist in dictonary") #printing message on console
        else: # else condition executed when length is not matching
            print("Please, enter correct string length word")
    else: #else condition executed when if condition checking for characters fails
        print("Please enter only alphabetical characters")

#calling the main method 
main()