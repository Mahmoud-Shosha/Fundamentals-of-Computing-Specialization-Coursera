# implementation of card game - Memory

import simplegui
import random

# Constants
cards = []
exposed = []
TEXT_SIZE = 60
TEXT_COLOR = 'white'
CARD_WIDTH = 50
state = 0
selected_cards = []
turns = 0


# helper function to initialize globals
def new_cards():
    l = range(8)
    random.shuffle(l)
    l += l
    random.shuffle(l)
    return l


def new_exposed():
    l = []
    for i in range(16):
        l.append(False)
    return l


def new_game():
    global cards, exposed, turns
    cards = new_cards()
    exposed = new_exposed()
    turns = 0


# define event handlers
def mouseclick(pos):
    global state, selected_cards, exposed, turns
    card_number = pos[0] // CARD_WIDTH
    changed_card = not exposed[card_number]
    if changed_card:
        if state == 0:
            exposed[card_number] = True
            selected_cards.append(card_number)
            state = 1
        elif state == 1:
            exposed[card_number] = True
            selected_cards.append(card_number)
            turns += 1
            state = 2
        else:
            if cards[selected_cards[0]] == cards[selected_cards[1]]:
                exposed[selected_cards[0]] = True
                exposed[selected_cards[1]] = True
            else:
                exposed[selected_cards[0]] = False
                exposed[selected_cards[1]] = False
            selected_cards = []
            exposed[card_number] = True
            selected_cards.append(card_number)
            state = 1


# cards are logically 50x100 pixels in size
def draw(canvas):
    x_pos = 0
    for i in range(len(cards)):
        if exposed[i]:
            canvas.draw_text(str(cards[i]), [x_pos + 9, 68], TEXT_SIZE, TEXT_COLOR)
        else:
            canvas.draw_polygon([[x_pos, 0], [CARD_WIDTH + x_pos, 0], [CARD_WIDTH + x_pos, 100], [x_pos, 100]], 2,
                                'gray', 'green')
        x_pos += CARD_WIDTH
    label.set_text("Turns = " + str(turns))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric