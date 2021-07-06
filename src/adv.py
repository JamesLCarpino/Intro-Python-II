from room import Room
from player import Player

# from item import Tissue
from item import Item
import time

# Declare all the rooms

room = {
    "outside": Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
        [
            Item(
                "A rock is stuck in your shoe, should not have worn sandles",
                "words",
                "words",
            )
        ],
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
        [
            Item(
                "Wad of Tissue",
                "This is disgusting wad of tissues, but on the back is what looks like a map...oh wait no thats a booger",
                "Not really important unless you really like boogers?",
            )
        ],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        [
            Item(
                "Compass",
                'It is a compass but it is broken, but it would not help anyway since all of the walls are made of iron. Thats rough. On the back of it it just has the reapeated words "Go back outside, go back outside go...back...outside..."',
                "Though it's broken, its could probably used to throw at something. Kinda important",
            )
        ],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        [
            Item(
                "Shovel",
                "It's a shovel, come on, you know what a shovel is.",
                "You don't know this yet, but I bet this is super important, but what do I know I just made the game.",
            )
        ],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        [
            Item(
                "Mappy McMappinson",
                "This map has the letters n - e - n, what could that possibly mean?",
                "Yeah probably not that important.",
            )
        ],
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]


# this lets me access items to put them into the room ie append
# tissue = Item(
#     "Wad of Tissue",
#     "This is disgusting wad of tissues, but on the back is what looks like a map...oh wait no thats a booger",
#     "Not really important unless you really like boogers?",
# )

# shovel = Item(
#     "Compass",
#     'It is a compass but it is broken, but it would not help anyway since all of the walls are made of iron. Thats rough. On the back of it it just has the reapeated words "Go back outside, go back outside go...back...outside..."',
#     "Though it's broken, its could probably used to throw at something. Kinda important",
# )
# room["foyer"].item.append(str(tissue))


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# might need this later, but not sure


# player object
# making an intro
def game_intro():
    print("You fell asleep...\n")
    time.sleep(1)
    print("...You may not remember falling asleep, but you did.\n")
    time.sleep(1)
    print(
        "This unfamliar grass is cool to the touch, but smells wrong. You rub your eyes and see that you don't recognize any of your surroundings.\n"
    )  # adjust this to be dynamic to the rooms dictionary
    print("A voice on the wind asks you a question")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.7)
    print("...")


# game_intro()

input_name = input("Hello, what is your name?: ")
player = Player(input_name, room["outside"], [])


print(f"{input_name},")

print(f"you are currently looking at the { player.current_room.name }...\n")
time.sleep(1)
print(f"looking around you take notice {player.current_room.description}")
time.sleep(1)
print(
    f"Patting your pockets to see what you've got on you and your inventory is: {player.inventory}"
)

movement = ""

# print(room["outside"].item)
while movement != "q":  # input validation
    movement = input(
        "which direction would you like to go? Enter n, s, e, w to move onward you brave son of a bitch\n...or be a litle sheepish lap dog and quit by hitting q: "
    )
    if movement == "n":
        if hasattr(player.current_room, "n_to"):
            player.current_room = player.current_room.n_to
            # player.current_room.has_item(tissue)
            print(f"You are now in the {player.current_room.name}...\n")
            print(f"checking your pockets you have {player.current_items()}")
            time.sleep(1)
            print(
                f"You look around the {player.current_room.name} and take notice that {player.current_room.description}"
            )
            print(
                f" Out of the corner of your eye you see a {player.current_room.item[0]}"
            )

        else:
            print("You can't go that direction, please choose another")
            input(
                "which direction would you like to go? Enter n, s, e, w to continue the journey, or q to shake yourself out of this fever dream: "
            )
    elif movement == "s":
        if hasattr(player.current_room, "s_to"):
            player.current_room = player.current_room.s_to
            print(f"You are now in the {player.current_room.name}...\n")
            time.sleep(1)
            print(
                f"You look around the {player.current_room.name} and take notice that {player.current_room.description} "
            )
            print(
                f"Out of the corner of your eye you see a {player.current_room.item[0]}"
            )
        else:
            print("You can't go that direction, please choose another")
            input(
                "which direction would you like to go? Enter n, s, e, w to continue the journey, or q to shake yourself out of this fever dream: "
            )
    elif movement == "e":
        if hasattr(player.current_room, "e_to"):
            player.current_room = player.current_room.e_to
            print(f"You are now in the {player.current_room.name}...\n")
            time.sleep(1)
            print(
                f"You look around the {player.current_room.name} and take notice that {player.current_room.description} "
            )
            print(
                f" Out of the corner of your eye you see a {player.current_room.item[0]}"
            )
        else:
            print("You can't go that direction, please choose another")
            input(
                "which direction would you like to go? Enter n, s, e, w to continue the journey, or q to shake yourself out of this fever dream: "
            )
    elif movement == "w":
        if hasattr(player.current_room, "w_to"):
            player.current_room = player.current_room.w_to
            print(f"You are now in the {player.current_room.name}...\n")
            time.sleep(1)
            print(
                f"You look around the {player.current_room.name} and take notice that {player.current_room.description} "
            )
            print(
                f" Out of the corner of your eye you see a {player.current_room.item[0]}"
            )
        else:
            print("You can't go that direction, please choose another")
            input(
                "which direction would you like to go? Enter n, s, e, w to continue the journey, or q to shake yourself out of this fever dream: "
            )
    elif movement == "q":
        time.sleep(1)
        print(
            "\nYou tried, you failed, but you tried.\nThat counts for something you quitter...I guess...\nThe cave closes behind you and you wake back up in your bed."
        )
        # time.sleep(2)
        # print(f"...{player.name} is a loser with a skinny weiner")
    elif movement == "pick":

        player.get_item(player.current_room.item[0])
        print(f"You picked up: {player.inventory}")
    elif movement == "check":
        player.current_items()
        if player.current_items() == []:
            print("you dont have any fucking gear you dingleberry!")
    else:
        print("Hey dingus, thats not a valid direction")
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
