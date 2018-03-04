# The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice. When the program runs, 
# it will randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the number of sides on the die is up to you.)
#  The program will print what that number is. It should then ask you if you’d like to roll again. For this project, you’ll need to set the min 
#  and max number that your dice can produce. For the average die, that means a minimum of 1 and a maximum of 6. You’ll also want a function that 
#  randomly grabs a number within that range and prints it.
# Reference: https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

# Author Sijan Shrestha
# Created on 3/4/2018

from random import randint

#Generating Random Number Between 1 and 6
def randomNum():
        r = randint(1, 6)
        return r

def main():
        
        #Printing Initial Random Dice Face
        x = randomNum()
        print("Rolled Face: " + str(x))
        
        #For Infinite Loop
        while(1) :
                choice = input("Do You Want To Roll Again? 'Y' OR 'N': ")
                #print(str(choice))
                
                #Checking User Preference
                if choice == 'Y' or choice == 'y':
                        x = randomNum()
                        print("Rolled Face: " + str(x))

                elif choice == 'N' or choice == 'n':
                        print("Quitting!")
                        break

                else:
                        print("Invalid choice..Please Enter 'Y' OR 'N'")
         
         #loop ends              
        print("Good Bye! :) ")

        

if __name__ == "__main__": main()
