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
class Flash_Card:
    def __init__(self):
        self.input = None
        self.output = None

    def set_input(self, input):
        self.input = input

    def set_output(self, output):
        self.output = output

def main():
    #Create an object
    Set_1 = Flash_Card()
    Set_1.set_input("2+2") #Modify its attributes with personal functions
    Set_1.set_output("4")

    #print attributes to console
    print(f"The input is {Set_1.input} and output is {Set_1.output}")

if __name__ == "__main__":
    main()