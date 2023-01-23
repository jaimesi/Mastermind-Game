"""
    Jaime Si
    CS5001 - Spring 2022
    Final Project - Testing Suite

    A testing suite that tests non-turtle functions from my version of the
    Mastermind game. Includes a function to test random combination generator,
    reading errors, and testing whether a leaderboard file exists or not.
"""
import random

def random_combination(colors, num):
    """
        Function to create random combination, from mastermind_game

        Note: I wasn't able to import this function from mastermind_game w/o
        turtle because I have the popup screen asking for the player's name as
        a global variable, which I also know is incorrect :/
    """
    
    combo = tuple(colors)
    number = len(combo)
    indices = sorted(random.sample(range(number), num))
    return tuple(combo[i] for i in indices)

def test_random_combination():
    """
        Test function that prints a random 4-length color combination
    """
    result_to_guess = random_combination \
                  (["blue","red","green","yellow","purple","black"], 4)
    
    print(result_to_guess)

def read_errors():
    """
        Test function that reads the error logger file, if any errors exist
    """

    print("Existing errors:\n")

    try:
        with open("mastermind_errors.err", mode="r") as f:
            for line in f:
                print(line)

    except IOError:
        print("Sorry, no error logger file found.")

def test_leaderboard():
    """
        Test function that prints out statement if a leaderboard file exists
    """
    with open("leaderboard.txt", "r") as f:
        for line in f:
            print(line)

def test_no_leaderboard():
    """
        Test function that prints out a statement if no leaderboard file found
    """
    try:
        f = open("leaderboard.txt","r")
        print("Leaderboard file found!")
    except IOError:
        print("No leaderboard file found.")

def main():

    # Tests to see if the program can generate random color combinations
    print("Testing random color combination generator:\n")
    test_random_combination()
    test_random_combination()
    test_random_combination()
    print("\n")

    # Test to print error messages
    read_errors()
    print("\n")

    # Test to print error when no leaderboard is found
    test_no_leaderboard() # File must be deleted on system to generate IOError
    print("\n")

    # Test to see if leaderboard file can be read
    print("Current leaderboard entries:\n")
    test_leaderboard()

if __name__ == "__main__":
    main()
