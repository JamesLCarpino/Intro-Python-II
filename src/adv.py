from room import Room
from player import Player
import time

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

#might need this later, but not sure



#player object
#making an intro
def game_intro():
    print('You fell asleep...\n')
    time.sleep(1)
    print('...You may not remember falling asleep, but you did.\n')
    time.sleep(1)
    print('This unfamliar grass is cool to the touch, but smells wrong. You rub your eyes and see that you don\'t recognize any of your surroundings.\n')# adjust this to be dynamic to the rooms dictionary
    print('A voice on the wind asks you a question')
    time.sleep(.5)
    print('.')
    time.sleep(.5)
    print('..')
    time.sleep(.7)
    print('...')

game_intro()    

input_name = input('Hello, what is your name?: ')
player = Player(input_name, room['outside'])

print(f'{input_name},')
print(f"you are currently looking at the { player.current_room.name }...\n")
time.sleep(1)
print(f'looking around you take notice {player.current_room.description}')
time.sleep(1)

movement = ''
while movement != 'q': #input validation
    movement = input('which direction would you like to go? Enter n, s, e, w to move onward you brave son of a bitch\n...or be a litle sheepish lap dog and quit by hitting q: ')
    if movement == 'n':
        if hasattr(player.current_room, 'n_to'):
            player.current_room = player.current_room.n_to
            print(f'You are now in the {player.current_room.name}...\n')
            time.sleep(1)
            print(f'You look around the {player.current_room.name} and take notice that {player.current_room.description} ')
        else:
            print('You can\'t go that direction, please choose another')
            input('which direction would you like to go? Enter n, s, e, w to continue the journey, or q to shake yourself out of this fever dream: ')
    elif movement == 's':   
        if hasattr(player.current_room, 's_to'):
            player.current_room = player.current_room.s_to
            print(f'You are now in the {player.current_room.name}...\n')
            time.sleep(1)
            print(f'You look around the {player.current_room.name} and take notice that {player.current_room.description} ')
        else:
            print('You can\'t go that direction, please choose another')
            input('which direction would you like to go? Enter n, s, e, w to continue the journey, or q to shake yourself out of this fever dream: ')    
    elif movement == 'e':
        if hasattr(player.current_room, 'e_to'):
            player.current_room = player.current_room.e_to
            print(f'You are now in the {player.current_room.name}...\n')
            time.sleep(1)
            print(f'You look around the {player.current_room.name} and take notice that {player.current_room.description} ') 
        else:
            print('You can\'t go that direction, please choose another')
            input('which direction would you like to go? Enter n, s, e, w to continue the journey, or q to shake yourself out of this fever dream: ')
    elif movement == 'w':
        if hasattr(player.current_room, 'w_to'):
            player.current_room = player.current_room.w_to
            print(f'You are now in the {player.current_room.name}...\n')
            time.sleep(1)
            print(f'You look around the {player.current_room.name} and take notice that {player.current_room.description} ')
        else:
            print('You can\'t go that direction, please choose another')
            input('which direction would you like to go? Enter n, s, e, w to continue the journey, or q to shake yourself out of this fever dream: ')
    elif movement == 'q':
        time.sleep(1)
        print('\nYou tried, you failed, but you tried.\nThat counts for something you quitter...I guess...\nThe cave closes behind you and you wake back up in your bed.')
        time.sleep(2)
        print(f'...{player.name} is a loser with a skinny weiner')
    else:
        print('Hey dingus, thats not a valid direction')
# Write a loop that:
#
# * Prints the current room name


    
# * Prints the current description (the textwrap module might be useful here).
   
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
