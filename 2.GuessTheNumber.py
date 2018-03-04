# The Goal: Similar to the first project, this project also uses the random module in Python. The program will first randomly generate 
# a number unknown to the user. The user needs to guess what that number is. (In other words, the user needs to be able to input information.) 
# If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low).
#  If the user guesses correctly, a positive indication should appear. You’ll need functions to check if the user input is an actual number,
#   to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.
# Reference: https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

# Author Sijan Shrestha
# Created on 3/4/2018


from random import randint

#Generating Random Number Between 1 and 6
def randomNum():
        r = randint(1, 9)
        return r

def userinput():
        usernum = input("Guess the number between 1 to 9: ")
        x = int(usernum)
        return x

def main():
        print("Welcome to Guess The Numer Game")
        print("")

        compnum = randomNum()
        #print(compnum)
        usernum = userinput()
        dif = compnum - usernum
        #print(dif)
        count = 1
        while( dif != 0):
                count = count + 1
                if dif < 0:
                        print("Too High")
                        usernum = userinput()
                        dif = compnum - usernum

                elif dif > 0:
                        print("Too Low")
                        usernum = userinput()
                        dif = compnum - usernum

        #print(count)
        print("You Guessed Correct Number i.e. " + str(compnum) + " at " + str(count) + " count!") 
        print("Thank You!")


if __name__ == "__main__": main()
