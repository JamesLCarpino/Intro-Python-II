# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        #rooms will be list of room instances
        self.rooms = self.init_current_rooms(rooms)
    
    def __str__(self):
        output = f'Hello weary adventurer! You are currently in {current_room}'
    
    #getting the room names and returning a list of room instances -> similarly to departments v stores
    def init_rooms(self, rooms):