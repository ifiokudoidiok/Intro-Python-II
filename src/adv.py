from room import Room
from player import Player


class Game:
    def __init__(self, room, player):
        self.room = room
        self.player = player

    def __str__(self):
        output = ''

        return 'output'


selection = ''
direction = ('n', 's', 'e', 'w')
while selection != 'q':
    selection = input(
        '\nEnter [n] for North \nEnter [s] for South \nEnter [e] for East \nEnter [w] for West \n')
    try:
        selection = str(selection)
        if selection == 'q':
            print("Goodbye")
        elif selection == 'n':
            print(f"You went North")
        elif selection == 's':
            print(f"You went South")
        elif selection == 'e':
            print(f"You went East")
        elif selection == 'w':
            print(f"You went West")
        else:
            print("Please enter a valid choice")
    except ValueError:
        print('Please enter a valid choice:\n [n]\n[s]\n[e]\n[w]')





# # Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

# #
# # Main
# #

# # Make a new player object that is currently in the 'outside' room.

# # Write a loop that:
# #
# # * Prints the current room name
# # * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.
# #
# # If the user enters a cardinal direction, attempt to move to the room there.
# # Print an error message if the movement isn't allowed.
# #
# # If the user enters "q", quit the game.
