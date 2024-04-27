import random
import time

RPS_set = ['R','P','S']
checkset = ['RP','PR','PS','SP','SR','RS','RR','PP','SS']
whowin = [0,1,0,1,0,1,2,2,2] #0 if first guy wins, 1 if second wins, 2 if tie

# bunch of interjenction words to add flavor to computers messages
with open("C:\CareerIT\Python\WordsListCareful\InterjectionsCareful.txt", 'r') as file:
    # Read the entire contents of the file into a string
    interj_words = file.readlines()
#ii = load('interjections.txt')
#print(interj_words[5])

def RPSgame():
    while True:
        
        # Computer Makes some noise (interjection) and Prompt the user to enter some input
        # print(random.choice(interj_words))
        user_input = input("Please enter your guess (or enter 'exit' to stop playing): ")
        # Print the input provided by the user
        print("You entered:", user_input)

        if user_input == "exit":
         break # stop playing the game if user enterred exit
    
        # Computer Selects a random RPS from the list
        computer_select = random.choice(RPS_set)
        computer_interj = random.choice(interj_words)
        
        print (" and I chose ... ")
        time.sleep(.5)

        print( computer_select , "!" )
        combine = user_input+computer_select

        #index = checkset.index(combine)
        if whowin[checkset.index(combine)] == 0:
            print(' so I win!...',computer_interj)
        elif whowin[checkset.index(combine)] == 1:
            print(' so You win!...',computer_interj)
        else:
            print('Well')
            time.sleep(.25)
            print('Its Tied!...', computer_interj) 
    
    print("Computer: Goodbye!")

RPSgame()    


       