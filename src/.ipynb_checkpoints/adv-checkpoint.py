from room import Room
from player import Player

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


player = Player("Bongo", room['outside'])
while True:
    print (f'You are in room {player.location}')
    action = input("Pick a direction n, s, e, w, q: ")
    if action == "n":
          next_room = player.location.n_to
    elif action == "s":
          next_room = player.location.s_to
    elif action == "e":
          next_room = player.location.e_to
    elif action == "w":
          next_room = player.location.w_to
    elif action == "q":
        print (f'Bye')
        break
    else:
        print (f'Forbidden direction')
        continue
    if next_room == None:
        print (f'No room here')
        continue
    player.location = next_room
    
      
    
    


"""
        Print the game info
"""
  
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#print current(initial state) of game

