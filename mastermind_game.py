"""
    Jaime Si
    CS5001 - Spring 2022
    Final Project

    A program that allows users to play a one player version of the game
    "Mastermind." By using turtle and starter files, players have 10 tries
    to guess a randomly generated 4-color combination. If players guess
    the correct code, their name and score is saved in a txt file that prints
    to the leaderboard when the program is restarted.

"""

from Marble import Marble
from Point import Point
from operator import itemgetter
from datetime import datetime
import turtle
import random

WINDOW = turtle.Screen() # Create the window

WINDOW_HEIGHT = 775 # Define window dimensions
WINDOW_WIDTH = 740

Y = 325 # y coordinate to place marbles
X = -290 # x coordinate to place marbles
X2 = -240 # x coordinate to place dots (red/black check marbles)

# Store the red and black circles
DOTS = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

# Store the marbles/circles
MARBLES = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]

# Define where the marbles input starts (first row, first column)
COUPLE = [0, 0]

MARBLE_SIZE = 1.7 # Size of the marbles (equivalent to radius of 15)
DOT_SIZE = 5 # Size of the red/black dots

# Store the different colored turtles
COLORS = [turtle.Turtle(),
        turtle.Turtle(),
        turtle.Turtle(),
        turtle.Turtle(),
        turtle.Turtle(),
        turtle.Turtle()]

# Dictionary that has the color as the key and the index as value
COLOR_MAP = {"blue": 0, "red": 1, "green": 2, "yellow": 3, "purple": 4,
             "black": 5}

PLAYER_NAME = WINDOW.textinput("CS5001 MasterMind", "Your Name:")

def window_setup():
    """
        Function -- window_setup
            Sets up dimensions of the turtle screen to the appropriate size
        Parameters: None
        Returns nothing
    """
    
    WINDOW.setup(WINDOW_WIDTH, WINDOW_HEIGHT) # Set dimensions of the screen

def register_buttons():
    """
        Function -- register_buttons
            Registers all GIFs as turtle shapes
        Parameters: None
        Returns nothing
    """
    
    WINDOW.register_shape("checkbutton.gif")
    WINDOW.register_shape("file_error.gif")
    WINDOW.register_shape("leaderboard_error.gif")
    WINDOW.register_shape("Lose.gif")
    WINDOW.register_shape("quit.gif")
    WINDOW.register_shape("quitmsg.gif")
    WINDOW.register_shape("winner.gif")
    WINDOW.register_shape("xbutton.gif")

def draw_rectangle(xpos, ypos, width, height, color):
    """
        Function -- draw_rectangle
            Draws a rectangle using a turtle at a specified location on the
            screen
        Parameters:
            xpos -- int -> the x coordinate to start drawing
            ypos -- int -> the y coordinate to start drawing
            width -- int -> the width of the rectangle to be drawn
            height -- int -> the height of the rectangle to be drawn
            color -- string -> the color of the rectangle's outline
        Returns nothing
    """
    
    rectangle = turtle.Turtle()

    rectangle.color(color)
    rectangle.hideturtle()
    rectangle.speed(0)
    rectangle.up()
    rectangle.goto(xpos, ypos)
    rectangle.down()
    rectangle.pensize(4)

    # Using a loop to draw the rectangle
    for i in range(2):
        rectangle.forward(width) 
        rectangle.left(90) 
        rectangle.forward(height) 
        rectangle.left(90)

def draw_board():
    """
        Function -- draw_board
            Draws the gameboard and reads the leaderboard file to display
            leaders. If no leaderboard txt file is found, a GIF error is
            displayed. In this case, users are still able to play the game
            and a new txt file will be created.
        Parameters: None
        Returns nothing 
    """

    register_buttons()

    # Draw rectangle with gameboard
    draw_rectangle(-360, -240, 450, 615, "Black")
    # Draw rectangle with leaderboard
    draw_rectangle(110, -240, 240, 615, "Blue")
    # Draw rectangle with controls
    draw_rectangle(-360, -375, 710, 120, "Black")

    # Initialize the leaderboard error message as a turtle
    leaderboard_error = turtle.Turtle()
    leaderboard_error.up()
    leaderboard_error.speed(0)
    leaderboard_error.shape("leaderboard_error.gif")
    leaderboard_error.goto(230, 300)
    leaderboard_error.hideturtle()

    # Initialize a turtle to write the leaderboard
    write_leaders = turtle.Turtle()
    write_leaders.up()
    write_leaders.hideturtle()
    write_leaders.speed(0)

    temp = []
    try:
        # Open and read the leaderboard txt file
        with open("leaderboard.txt", mode="r") as leaderboard:
            for line in leaderboard:
                # Save score as name, score
                temp.append(line.strip().split(", "))
            # Close file after reading
            leaderboard.close()
            write_leaders.goto(140, 330)
            write_leaders.down()
            write_leaders.write("Leaders:", font=('Arial', 14))
            write_leaders.up()
            # Show the top 5 scores
            for i in range(len(temp[:5])):
                write_leaders.goto(140,290-40*i)
                write_leaders.down()
                write_leaders.write(temp[i][0], font=('Arial', 14))
                write_leaders.up()
    except IOError as e:
        # Show GIF if leaderboard txt is not found
        leaderboard_error.showturtle()

    write_leaders.up()

def place_marbles():
    """
        Function -- place_marbles
            Draws marbles on the turtle screen to represent a 4 x 10 grid,
            one grid for the colored marbles, and one grid for the black and
            red dots
        Parameters: None
        Returns nothing
    """

    # Create the grid to place the marbles in their correct spots
    for i in range(10):
        for j in range(4):
            MARBLES[i][j] = Marble(Point(X + 45 * j, Y - 60 * i), "white")
            MARBLES[i][j].draw_empty()

    y = Y + 15
    for i in range(10):
        for j in range(4):
            DOTS[i][j] = Marble(Point(X2 + 180 + 10 * (j % 2), y - 10 *
                                      (j // 2)), "white", size = DOT_SIZE)
            DOTS[i][j].draw_empty()
        y = y - 60

def place_circles():
    """
        Function -- place_circles
            Places the 6 colored circles in a row for users to select, filled
        Parameters: None
        Returns nothing
    """

    # Set turtle speed and shape for the colored buttons
    for element in COLORS:
        element.speed(0)
        element.hideturtle()
        element.shape("circle")

    # Draw colored buttons
    for i in range(len(COLORS)):
        COLORS[i].up()
        COLORS[i].goto(-290 + 45 * i, -315) # Space the circles equally
        COLORS[i].turtlesize(MARBLE_SIZE)
        COLORS[i].showturtle()

    # Set the marble colors
    COLORS[0].color("blue", "blue")
    COLORS[1].color("red", "red")
    COLORS[2].color("green", "green")
    COLORS[3].color("yellow", "yellow")
    COLORS[4].color("purple", "purple")
    COLORS[5].color("black", "black")


"""
    The following 6 functions are used to place the marbles in the correct
    positions when the user clicks on the screen.

    Functions -- place_color1, place_color2, place_color3, place_color4,
                 place_color5, place_color6
    Parameters: x and y (coordinates of screen where user clicks with mouse)
    Returns nothing
"""

def place_color1(x, y):

    # If the color or marble was already selected, we move to the next
    if COUPLE[1] > 3 or COLORS[0].fillcolor() == "white":
        return
    else:
        MARBLES[COUPLE[0]][COUPLE[1]].set_color(COLORS[0].pencolor())
        MARBLES[COUPLE[0]][COUPLE[1]].draw()
        # "Remove" fill color of the marble (change to white)
        COLORS[0].fillcolor("white")
        COUPLE[1] += 1

def place_color2(x, y):
    
    if COUPLE[1] > 3 or COLORS[1].fillcolor() == "white":
        return
    else:
        MARBLES[COUPLE[0]][COUPLE[1]].set_color(COLORS[1].pencolor())
        MARBLES[COUPLE[0]][COUPLE[1]].draw()
        COLORS[1].fillcolor("white")
        COUPLE[1] += 1

def place_color3(x, y):
    
    if COUPLE[1] > 3 or COLORS[2].fillcolor() == "white":
        return
    else:
        MARBLES[COUPLE[0]][COUPLE[1]].set_color(COLORS[2].pencolor())
        MARBLES[COUPLE[0]][COUPLE[1]].draw()
        COLORS[2].fillcolor("white")
        COUPLE[1] += 1

def place_color4(x, y):
    
    if COUPLE[1] > 3 or COLORS[3].fillcolor() == "white":
        return
    else:
        MARBLES[COUPLE[0]][COUPLE[1]].set_color(COLORS[3].pencolor())
        MARBLES[COUPLE[0]][COUPLE[1]].draw()
        COLORS[3].fillcolor("white")
        COUPLE[1] += 1

def place_color5(x, y):
    
    if COUPLE[1] > 3 or COLORS[4].fillcolor() == "white":
        return
    else:
        MARBLES[COUPLE[0]][COUPLE[1]].set_color(COLORS[4].pencolor())
        MARBLES[COUPLE[0]][COUPLE[1]].draw()
        COLORS[4].fillcolor("white")
        COUPLE[1] += 1

def place_color6(x, y):
    
    if COUPLE[1] > 3 or COLORS[5].fillcolor() == "white":
        return
    else:
        MARBLES[COUPLE[0]][COUPLE[1]].set_color(COLORS[5].pencolor())
        MARBLES[COUPLE[0]][COUPLE[1]].draw()
        COLORS[5].fillcolor("white")
        COUPLE[1] += 1

def quit_button_fun(x, y):
    """
        Function -- quit_button_fun
            Turtle to display quit message
        Parameters: x and y -- coordinates of screen where user clicks with
                    mouse
        Returns nothing
    """

    quitmsg = turtle.Turtle()
    quitmsg.up()
    quitmsg.speed(0)
    quitmsg.shape("quitmsg.gif")

def x_button_fun(x,y):
    """
        Function -- quit_button_fun
            Deletes current selected marble one at a time
        Parameters: x and y -- coordinates of screen where user clicks with
                    mouse
        Returns nothing
    """

    # If there is no active marble
    if COUPLE[1] == 0:
        return
    else:
        # Delete one marble at a time
        temp = MARBLES[COUPLE[0]][COUPLE[1] - 1].get_color()
        MARBLES[COUPLE[0]][COUPLE[1] - 1].draw_empty()
        # Fill the deleted marble with the original color
        COLORS[COLOR_MAP[temp]].fillcolor(temp)
        COUPLE[1] -= 1

def random_combination(colors, num):
    """
        Function -- random_combination
        Parameters:
            colors -- list -> list of colors to choose from
            num -- int -> length of combination to generate
        Returns random colors as a tuple
    """

    # Convert to tuple
    combo = tuple(colors)
    number = len(combo)
    indices = sorted(random.sample(range(number), num))
    return tuple(combo[i] for i in indices)

result_to_guess = random_combination \
                  (["blue","red","green","yellow","purple","black"], 4)

def check_winning_conditions():
    """
        Function -- check_winning_conditions
        
        Parameters: None
        Returns True if the current element matches the current result_to_guess
        Returns False otherwise
    """

    i = 0
    for element in result_to_guess:
        if MARBLES[COUPLE[0]][i].get_color()!= element:
            return False
        # Move on to the next marble
        i += 1
    return True

def check_correct_answers():
    """
        Function -- check_correct_answers
            Checks each element in the selected marbles to see if they match
            with result_to_guess
        Parameters: None
        Returns nothing
    """

    # Initialize list to check correct marble placement
    marble_list = []
    
    for element in MARBLES[COUPLE[0]]:
        marble_list.append(element.get_color())

    i = 0
    # Set all correctly chosen colors to red
    for element in result_to_guess:
        if element in marble_list:
            DOTS[COUPLE[0]][i].set_color("red")
            DOTS[COUPLE[0]][i].draw()
            i += 1

    i = 0
    j = 0
    # Set all correctly chosen colors AND positions to black (overwrite)
    for element in result_to_guess:
        if MARBLES[COUPLE[0]][j].get_color() == element:
            DOTS[COUPLE[0]][i].set_color("black")
            DOTS[COUPLE[0]][i].draw()
            i += 1
        j += 1

def save_leaderboard(new_text):
    """
        Function -- save_leaderboard
            Reads the current leaderboard txt file and sorts the entries for
            best score. Writes new scores into the file. If a leaderboard file
            doesn't exist and the user figures out the color combination, one
            is created and the score is added
        Parameters:
            new_text -- str -> the name of the new text file to create
        Returns nothing
        
    """

    register_buttons()

    # Create the turtle that displays the error message
    file_error = turtle.Turtle()
    file_error.up()
    file_error.speed(0)
    file_error.shape("file_error.gif")
    file_error.hideturtle()
    
    temp = []

    try:
        with open("leaderboard.txt", mode="r") as leaderboard:
            for line in leaderboard:
                # Sort the list by the number in index 1
                temp = sorted(temp, key=itemgetter(1))
                temp.append(line.strip().split(","))
                
        # Save the current winners
        temp.append([PLAYER_NAME, str(COUPLE[0] + 1)])
        # Sort again by index 1 (score)
        temp = sorted(temp, key=itemgetter(1))
        with open("leaderboard.txt", mode="w") as leaderboard:
            for line in temp:
                # Write each line as player, score
                leaderboard.write(line[0] + "," + line[1] + "\n")
            leaderboard.close()

    # If a leaderboard.txt file doesn't exist, create one
    except Exception as e:
        temp.append([PLAYER_NAME, str(COUPLE[0]+1)])
        with open(new_text, mode="w") as new:
            for line in temp:
                new.write(line[0] + "," + line[1] + "\n")
            new.close()
        # Write any errors that come up to the .err file
        with open("mastermind_errors.err", mode="w") as errors:
            errors.write(str(e) + "," + str(datetime.now()) + "\n")

def check_button_fun(x, y):
    """
        Function -- check_button_fun
            If users do not select 4 colors, nothing happens.
            If users are on their last try, a winner message will pop up and
            save their score to the leaderboard if they succeed. Otherwise,
            a lose message will pop up and the game will be over.
            After each try, the buttons on the user control panel are reset to
            their original colors.
        Parameters: x and y -- coordinates of screen where user clicks with
                    mouse
        Returns nothing
    """

    register_buttons()

    # Create turtles to display appropriate win/lose message
    winner_msg = turtle.Turtle()
    winner_msg.up()
    winner_msg.speed(0)
    winner_msg.shape("winner.gif")
    winner_msg.hideturtle()

    lose_msg = turtle.Turtle()
    lose_msg.up()
    lose_msg.speed(0)
    lose_msg.shape("Lose.gif")
    lose_msg.hideturtle()

    # If users do not select 4 colors, nothing happens
    if COUPLE[1]!= 4:
        return
    # If this is the user's final chance (9th try)
    elif COUPLE[0] == 9:
        if check_winning_conditions() is True:
            # Save name and score to leaderboard, display winner message
            save_leaderboard("leaderboard.txt")
            winner_msg.showturtle()
            return
        else:
            # Display lose message
            lose_msg.showturtle()
            return
    # If this is user's chance 1 through 8
    else:
        if check_winning_conditions() is True:
            save_leaderboard("leaderboard.txt")
            winner_msg.showturtle()
            return
        else:
            # If user did not select the right combination, display red/black
            check_correct_answers()
            COUPLE[0] += 1
            COUPLE[1] = 0

    # Reset the colored marble buttons
    for temp in COLOR_MAP:
        COLORS[COLOR_MAP[temp]].fillcolor(temp)

def main():

    register_buttons()
    
    window_setup()
    try:
        
        draw_board() # Draw board
        place_marbles() # Draw marbles and circles
        place_circles()

        # Initialize check button as a turtle
        checkbutton = turtle.Turtle()
        checkbutton.up()
        checkbutton.speed(0)
        checkbutton.shape("checkbutton.gif")
        checkbutton.hideturtle()

        # Initialize x button as a turtle
        xbutton = turtle.Turtle()
        xbutton.up()
        xbutton.speed(0)
        xbutton.shape("xbutton.gif")
        xbutton.hideturtle()

        # Initialize quit button as a turtle
        quitbutton = turtle.Turtle()
        quitbutton.up()
        quitbutton.speed(0)
        quitbutton.shape("quit.gif")
        quitbutton.hideturtle()

        # Place buttons in the appropriate place
        checkbutton.goto(40, -315)
        checkbutton.showturtle()
        xbutton.goto(130,-315)
        xbutton.showturtle()
        quitbutton.goto(260, -315)
        quitbutton.showturtle()

        WINDOW.listen()

        # Place marbles in correct places when clicked
        COLORS[0].onclick(place_color1)
        COLORS[1].onclick(place_color2)
        COLORS[2].onclick(place_color3)
        COLORS[3].onclick(place_color4)
        COLORS[4].onclick(place_color5)
        COLORS[5].onclick(place_color6)

        # If the quit button is clicked, message pops up
        quitbutton.onclick(quit_button_fun)
        # If the x button is clicked, the previous color choice is deleted
        xbutton.onclick(x_button_fun)
        # If the check button is clicked, the program checks for correct answer
        checkbutton.onclick(check_button_fun)

        WINDOW.mainloop()
    except Exception as e:
        # Write errors to error logger file
        with open("mastermind_errors.err", mode="w") as errors:
            errors.write(str(e) + "," + str(datetime.now()) + "\n")

if __name__ == "__main__":
    main()
