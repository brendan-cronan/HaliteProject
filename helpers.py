import hlt

# This library contains constant values.
from hlt import constants

# This library contains direction metadata to better interface with the game.
from hlt.positionals import Direction

# This library allows you to generate random numbers.
import random

# Logging allows you to save messages for yourself. This is required because the regular STDOUT
#   (print statements) are reserved for the engine-bot communication.
import logging

def find_cluster(game_map,threshold):
    # x=0;
    # y=0;
    # pos=Position(x,y);
    for x in range(0, constants.WIDTH):
        for y in range(0, constants.HEIGHT):
            pos = Position(x,y);

            if game_map[pos].halite_amount >= 500:

                adjacent_positions = check_adjacent(x,y);
                total_surrounding = 0;
                # sum up all of the surrounding halite.
                for position in adjacent_positions:
                    total_surrounding+=position[1];

                if total_surrounding >= threshold:
                    return pos;

        return Position(-1,-1);



"""
Return:
[
    [Position, halite_amount]
    [Position, halite_amount]
]
"""
def check_adjacent(x,y):
"""
Return:
[
    Position, amount
]
"""
def highest_adjacent(x,y):
