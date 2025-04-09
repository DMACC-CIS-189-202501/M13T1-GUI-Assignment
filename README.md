# M13 T1: GUI Assignment

## Instructions for students

- Implement your solutions in `assignment.py`
- The tests in `test_assignment.py` can be inspected but do not modify them

### Directions - Copy/Pasted from Canvas

* With buttons each numbered 1 to MAX. You can select 10 or more buttons for this, deciding at design time.
* With a button 'Start Game'
* Generates a random number between 1 and MAX.
* Resets games
* Allow user to push button with their corresponding guess.
  * If correct guess: Create a WINNER window or messagebox to pop up
    * Reset game
  * Else
    * Set the button to visible but not clickable
    * Add guessed number to guessed_list in object of type NumberGuesser
* Write a class NumberGuesser.
  * guessed_list - class attribute contains all the guessed numbers, should be empty on new game or reset game
  * add_guess - class method that will add to the guessed_list
* Write a unit test for NumberGuesser
  * setUp() and tearDown()
  * test constructor
  * test adding to guessed_list