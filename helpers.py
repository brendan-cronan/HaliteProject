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


"""
    Algorithm for choosing the proper mining locationself.
    To be executed every turn and by definition, executes with every ship in mind.
"""
def choose_target_mine(game_map,ship_locations):
    for x in range(0, constants.WIDTH):
        for y in range(0, constants.HEIGHT):
            pos = Position(x,y)
            loc = game_map[pos]

            #these are values that only need to be calculated once per tile.
            dist_to_yard = dist_to_shipyard(pos)
            dist_to_closest_dropoff = find_nearest_dropoff(pos)
            halite_amt = loc.halite_amount;


            #creates a dictionary to store the ship id and its current best score.
            best_score = {}
            for ship in me.get_ships():
                #loop through all ships and set each value to init 0.
                best_score[ship.id] = 0


            #calculating the score for this tile for each ship.
            for ship in me.get_ships():
                score = mine_scoring_function(loc, ship, dist_to_yard, halite_amt)
                if score > best_score[ship.id]:
                    best_score[ship.id] = score

                    #TODO This Also needs to 'claim' this tile so other ships don't take it.
                        #unless they have an even higher score for this tile?






"""
Given a position, dist from shipyard, dist to ship, halite amount,
returns a "score"
"""
def mine_scoring_function( pos, ship, yard_dist, halite_amt):
    ship_dist = game_map.calculate_distance(pos, ship.position)






""" Returns the distance from given pos to the shipyard for ease of use. """
def dist_to_shipyard(pos):
    return game_map.calculate_distance(pos, me.shipyard.position)

"""
Code for finding the closest dropoff point.  Not relevant until dropoffs are implemented.
"""
def find_nearest_dropoff(pos):
    if me.get_dropoffs() = []:
        return None
    dist_to_closest_dropoff = 999
    for dropoff in me.get_dropoffs():
        dist = game_map.calculate_distance(pos, dropoff)
        if dist < dist_to_closest_dropoff:
                dist_to_closest_dropoff =dist
        if dist_to_closest_dropoff == 999:
            return None








"""
Function to determine if a certain space is currently inspired.
Returns a boolean value indicating if it is inspired or not.
"""
def is_inspired(pos):









def find_cluster(game_map,threshold):
    # x=0
    # y=0
    # pos=Position(x,y)
    for x in range(0, constants.WIDTH):
        for y in range(0, constants.HEIGHT):
            pos = Position(x,y)

            if game_map[pos].halite_amount >= 500:

                adjacent_positions = check_adjacent(x,y)
                total_surrounding = 0
                # sum up all of the surrounding halite.
                for position in adjacent_positions:
                    total_surrounding+=position[1]

                if total_surrounding >= threshold:
                    return pos

    return Position(-1,-1)



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
