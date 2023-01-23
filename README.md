# Mastermind Game  

Welcome to my version of Mastermind! This was my first Python project created for CS5001 - Introduction to Computer Science at Northeastern University. 
I hope you enjoy!  

### How to Play  

Mastermind, also known as Bulls and Cows, is a code-breaking puzzle game. The player has 10 tries to figure out the code combination.  

In this version of Mastermind, the user will be prompted for their name. Once entered, the game board will load. To play:  
  - Choose 4 colors, in any order
  - Once chosen, click the check mark. One of three colors will appear to the right of the row: Red, Black, and White.
      - Red: the color is correct, but in the wrong spot
      - Black: the color is correct and in the correct spot
      - White: the color is incorrect
  - Keep guessing until all four dots return as black. **Note!** Receiving a black dot in the first slot does not necessarily mean your first chosen color is correct. It means *any* of the four colors is correct.
  - Did you figure out the combination? *Congratulations!* Next time you open the game, your name and the number of attempts it took you to crack the code will appear on
  the leaderboard. Challenge your friends in Mastermind and keep playing to beat each other's scores!
  
  ### Future Improvements  
  
  - The game seems to be pretty glitchy at times. Different GIF messages pop up for a split second before the correct one is displayed
  - When the user clicks on the check button but doesn't select 4 different colors, the game still works, but all of the GIF buttons disappear until another marble is clicked
  - I had trouble creating a pointer image that worked consistently, so I decided to take it out altogether
  - I would like to try to create this game in the future using only one global turtle instead of a separate turtle for every component of the game
