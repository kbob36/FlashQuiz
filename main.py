"""
Study Project
By: Kian Venter
Created:2025-04-18

TODO: 
Practice functions and objects
Find UI Options
Learn AI API
Start Developping Framework

"""

"""
Class used for all flash card objects

The idea here is to create an object for each flashcard that the student
can add information too
"""
class Flashcard:
    def __init__(self, number):
        self.number = number
        self.input = None
        self.output = None

    def set_input(self, input):
        self.input = input

    def set_output(self, output):
        self.output = output

def main():
    #To create number of flash cards
    Num_Cards = 0

    #Prompt the user for the number of flashcards they wish to make
    Num_Cards = input("How many flash cards will you create?")
    Num_Cards = int(Num_Cards)

    #Create a list containing all flash cards
    Flashcards = [Flashcard(i) for i in range(Num_Cards)]

    print(f"You have {Num_Cards} flash cards")
    print("Please fill a flash card")

    #Receive input for the first flash card
    Flashcards[0].input = input("What would you like the fact to be?")
    Flashcards[0].output = input("What is the solution to this card")

    #print attributes to console
    print(f"The question is: {Flashcards[0].input} and the answer is: {Flashcards[0].output}")

if __name__ == "__main__":
    main()