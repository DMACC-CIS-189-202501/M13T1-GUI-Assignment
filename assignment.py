# TODO 1: Delete this and enter your DocString

import tkinter
from number_guesser import NumberGuesser
import random

# TODO set max to a number that is 10 or greater for the number of buttons you have
MAX = 10
winning_number = -1
#TODO, do you need anything to initialize NumberGuesser?
num_guess = NumberGuesser()

# --- Start Function Defs Here

# TODO verify if get_random_winner is correct
# Randomly generates a winning Number between 1 and MAX, ?inclusive?
def get_random_winner():
    global winning_number
    global MAX
    winning_number = random.randint(1,MAX)

def start_game():
    # undisable all guess buttons
    _undisable_all_guess_buttons()
    #undisable reset
    reset_game_button["state"] = "normal"
    #disable start game button
    new_game_button["state"] = "disable"
    # Generate a random winner
    get_random_winner()

def reset_game():
    #disable all guess buttons
    _disable_all_guess_buttons()
    #disable reset
    reset_game_button["state"] = "disable"
    #undisable start game button
    new_game_button["state"] = "normal"

# TODO add/modify or write your own method to enable/disable buttons
def _undisable_all_guess_buttons():
    guess_one_button["state"] = "normal"
    guess_two_button["state"] = "normal"


# TODO add/modify or write your own method to enable/disable buttons
def _disable_all_guess_buttons():
    guess_one_button["state"] = "disable"
    guess_two_button["state"] = "disable"


# TODO: This method is incomplete, figure out how you would like to code this
# you can repeat some code a lot, write your own function, write a helper function, etc
def guess_one():
    # Disable button
    guess_one_button["state"] = "disable"
    #Add Guess
    num_guess.add_guess(1)
    # TODO Check if we won; if we did, display a box that we won
    # If not, continue on

# TODO: This method is incomplete, figure out how you would like to code this
# you can repeat some code a lot, write your own function, write a helper function, etc
def guess_one():
    # Disable button
    guess_one_button["state"] = "disable"
    #Add Guess
    num_guess.add_guess(1)
    # TODO Check if we won; if we did, display a box that we won
    # If not, continue on

# TODO: This method is incomplete, figure out how you would like to code this
# you can repeat some code a lot, write your own function, write a helper function, etc
def guess_two():
    # Disable button
    guess_two_button["state"] = "disable"
    #Add Guess
    num_guess.add_guess(2)
    # TODO Check if we won; if we did, display a box that we won
    # If not, continue on


# --- End Function Defs



# Ideally this would be main_gui_window = tkinter.Tk(), but that is a lot to type over and over;
# so we will use 'm'
m = tkinter.Tk()

m.title('Number Guesser Game')

new_game_button = tkinter.Button(m, text="Start Game", command=start_game)
new_game_button.grid(row=1, column=1)

reset_game_button = tkinter.Button(m, text="Reset Game", command=reset_game, state="disabled")
reset_game_button.grid(row=1, column=2)

# Note state is initially set to disabled when window opens
guess_one_button = tkinter.Button(m, text="1", command=guess_one, state="disabled")
guess_one_button.grid(row=3, column=1)
guess_two_button = tkinter.Button(m, text="2", command=guess_two, state="disabled")
# TODO, define your own button layout, you can have them all in 1 row, in 3x3 layout, 2x5, etc
guess_two_button.grid(row=3, column=2)


# TODO define an exit button

# At the very end, this closes the loop and starts the GUI...however it is wrapped into a main driver so autograding code will work.
if __name__ == "__main__":
    m.mainloop()


