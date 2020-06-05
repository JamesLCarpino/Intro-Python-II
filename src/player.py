# Write a class to hold player information, e.g. what room they are in
# currently.
import item


class Player:
    def __init__(self, name, current_room, inventory=[], item=[]):
        self.name = name
        # rooms will be list of room instances
        self.current_room = current_room
        self.inventory = inventory

    def current_items(self):
        for item in self.inventory:
            print(item, "\n")

    def get_item(self, newItem):
        self.inventory.append(newItem)
        return f"You picked up {newItem} and have it in your inventory. Great. If its the Tissue thats gross."

    def __str__(self):
        return f"{self.name} {self.description} {self.inventory}"

    # getting the room names and returning a list of room instances -> similarly to departments v stores
