# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

num_range = 100


# helper function to start and restart the game
def new_game():
    """
    Set the global secret_number accoring to
    the choosen global num_range
    """

    global secret_number, guesses_number

    if num_range == 100:
        guesses_number = 7
    elif num_range == 1000:
        guesses_number = 10

    secret_number = random.randrange(0, num_range)

    print "New game. Range is [0," + str(num_range) + ")"
    print "Number of remaining guesses is " + str(guesses_number)
    print


# define event handlers for control panel
def range100():
    """Change the global num_range to 100"""

    global num_range

    num_range = 100

    new_game()


def range1000():
    """Change the global num_range to 1000"""

    global num_range

    num_range = 1000

    new_game()


def input_guess(guess):
    """
    Print the guess to the console, and
    Determine whether Higher, Lower or Correct
    """

    global secret_number, guesses_number

    guess = int(guess)

    print "Guess was ", str(guess)

    guesses_number -= 1

    print "Number of remaining guesses is " + str(guesses_number)

    if secret_number == guess:
        print "Correct !"
        print
        new_game()
    elif guesses_number == 0:
        print "You ran out of guesses.  The number was " + str(secret_number)
        print
        new_game()
    elif secret_number > guess:
        print "Higher !"
    elif secret_number < guess:
        print "Lower !"

    print


# create frame
frame = simplegui.create_frame("Guess the number !", 300, 250)

# register event handlers for control elements and start frame
frame.add_button("Range is  [0, 100)", range100)
frame.add_button("Range is  [0, 1000)", range1000)
frame.add_input("Enter the guss", input_guess, 120)

# call new_game
new_game()

# always remember to check your completed program against the grading rubric

