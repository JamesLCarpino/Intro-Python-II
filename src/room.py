# Implement a class to hold room information. This should have name and
# description attributes.

# room object
# import item


class Room:
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item

    def __str__(self):
        return f"{self.name} {self.description} {self.item}"

    def has_item(self, room_item):
        # self.item.append(room_item)
        return f"{self.room_item}"
