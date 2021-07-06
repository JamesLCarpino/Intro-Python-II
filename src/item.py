# class Item(Room):
#     def __init__(self, item_name, i_description):
#         super().__init__(self, name, description)
#         self.item_name = item_name
#         self.i_description = i_description


# class Item(Player):
#     def __init__(self, i_name, i_description)
#         super().__init__(name, current_room)
#         self.i_name = i_name
#         self.i_description = i_description


class Item:
    def __init__(self, name, description, importance):
        self.name = name
        self.description = description
        self.importance = importance

    def __str__(self):
        return f"{self.name}\n\n{self.description}\n\n{self.importance}"


# class Tissue(Item):
#     def __init__(self, name, description, value):
#         super().__init__(name, description)
#         self.value = value

#     def __str__(self):
#         return f"{self.name} {self.description}"


# class Compass(Item):
#     def __init__(self, importance):
#         self.importance = importance
#         super().__init__(
#             name="Compass",
#             description='It is a compass but it is broken, but it would not help anyway since all of the walls are made of iron. Thats rough. On the back of it it just has the reapeated words "Go back outside, go back outside go...back...outside..."',
#             importance="Though it's broken, its could probably used to throw at something. Kinda important",
#         )


# class Shovel(Item):
#     def __init__(self, importance):
#         self.importance = importance
#         super().__init__(
#             name="Shovel",
#             description="It's a shovel, come on, you know what a shovel is.",
#             importance="You don't know this yet, but I bet this is super important, but what do I know I just made the game.",
#         )


# class Map(Item):
#     def __init__(self, importance):
#         self.importance = importance
#         super().__init__(
#             name="Mappy McMappinson",
#             description="This map has the letters n - e - n, what could that possibly mean?",
#             importance="Yeah probably not that important.",
#         )
