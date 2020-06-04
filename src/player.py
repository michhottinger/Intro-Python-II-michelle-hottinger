# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    
    new_position = """needs some value here"""
    
    
    def __init__(self, name, room):
        self.name = name 
        self.room = room

    def move_player(self):
        self.room = self.new_position
    
    def print_player(self):
        return '{} is playing in room {} which looks like {}'.format(self.name, self.room, self.description)
    
    