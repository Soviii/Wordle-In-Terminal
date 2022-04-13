#  Wordle in Terminal

# About 
This game imitates the notorious word-guessing game - **Wordle**. While it is obviously not 
a 1-on-1 copy, it was a fun project to do for learning Python and creating my first game with. 
It took me about a day in total to finish creating this and anyone with Python3 is able to play it on their machine!


# Development Process
It utilizes two text files - one for verifying the user's input if it is an actual word and another for choosing the targeted word. By the standards
of the game, the chosen word will always be a five-character word. 

Using the curses modules, windows were made for each attempt and for displaying the instructions as well as the status of each input (when the enter key
is pressed). As to the user input, it is restricted to certain a certain list of keystrokes. If the user enters a keystroke that is found in the list,
it will be displayed and added to the string on the screen. I created 3 color pairs for the background of each letter - one for incorrect and user inputs, 
another for correct letter but wrong placement, and another for correct letter and placement for a character. When a valid, real word is inputed and the user
presses "enter", the word is compared to the chosen word in which each letter from the inputed string is ran through one or two tests functions. If a character 
passes one of the two tests, then it will have either a green background or a yellow background. The first one checks if the character is in the chosen word along 
with in the right placement. If this function returns true, then the background of the character is green, indicating that this character is correct. If this test 
function fails, the next test function is called. If the current character is found in the chosen word, then it will return true in which the character will now have
a yellow background. If a letter from the inputed word does not pass any test, then it will default to the white background, meaning the letter does not exist in the 
chosen word. To give it some visual effects, I also added the time module to use the sleep() function to pause the program so it gives it a delayed effect when showing
the accuracy of each character. For each attempt, these test functions will run. If the user guesses the chosen word correctly, then the program will display a "Good Job"
message and will end once a keystroke is entered. On the other hand, if the user does not guess it correctly, then it will display the chosen word and the program will
end on the next keystroke. 


