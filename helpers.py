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
    Algorithm for choosing the proper mining location.
    To be executed every turn and by definition, executes with every ship in mind.
"""
def choose_target_mine(game,ship_locations):
    me = game.me
    game_map = game.game_map
    inspired_tiles = inspired_grid(game_map)
    for x in range(0, constants.WIDTH):
        for y in range(0, constants.HEIGHT):
            pos = Position(x,y)
            loc = game_map[pos]

            #these are values that only need to be calculated once per tile.
            dist_to_yard = dist_to_shipyard(game_map,pos)
            dist_to_closest_dropoff = find_nearest_dropoff(game_map,pos)
            halite_amt = loc.halite_amount


            #creates a dictionary to store the ship id and its current best score.
            best_score = {}
            for ship in me.get_ships():
                #loop through all ships and set each value to init 0.
                best_score[ship.id] = 0


            #calculating the score for this tile for each ship.
            for ship in me.get_ships():
                score = mine_scoring_function(game_map,loc, ship, dist_to_yard, halite_amt)
                if score > best_score[ship.id]:
                    best_score[ship.id] = score

                    #TODO This Also needs to 'claim' this tile so other ships don't take it.
                        #unless they have an even higher score for this tile?






"""
Given a position, dist from shipyard, dist to ship, halite amount,
returns a "score"
"""
def mine_scoring_function(game_map, pos, ship, yard_dist, halite_amt):
    ship_dist = game_map.calculate_distance(pos, ship.position)






""" Returns the distance from given pos to the shipyard for ease of use. """
def dist_to_shipyard(game_map, pos):
    return game_map.calculate_distance(pos, me.shipyard.position)

"""
Code for finding the closest dropoff point.  Not relevant until dropoffs are placed.
Returns the distance to shipyard if no dropoffs are found
"""
def find_nearest_dropoff(game_map,pos):
    if me.get_dropoffs() = []:
        return dist_to_shipyard(game_map,pos)

    dist_to_closest_dropoff = dist_to_shipyard(game_map,pos)

    for dropoff in me.get_dropoffs():
        dist = game_map.calculate_distance(pos, dropoff.position)
        if dist < dist_to_closest_dropoff:
                dist_to_closest_dropoff = dist
        if dist_to_closest_dropoff == 999:
            return None








"""
Function to determine if What spaces on the board are inspired.
Should be calculated once per turn.
Return:
    2D Array of boolean True/False values indicating whether a position is inspired or not.
    ex.
        [
            [True, True, False, False False]
            [True, True, False, False False]
            [True, True, False, False False]
            [True, True, False, False False]
        ]
"""
def inspired_grid(game_map):
    inspiration = [constants.HEIGHT][constants.WIDTH]

    for x in range(constants.WIDTH):
        for y in range(constants.HEIGHT):

            pos = Position(x,y)
            enemies = 0;

            if check_adjacent_enemies(game_map,pos.x,pos.y, constants.INSPIRATION_RADIUS) >= Constants.INSPIRATION_SHIP_COUNT
                inspiration[pos.x][pos.y] = True
            else:
                inspiration[pos.x][pos.y] = False

    return inspiration;








def find_cluster(game_map,threshold):
    # x=0
    # y=0
    # pos=Position(x,y)
    for x in range(0, constants.WIDTH):
        for y in range(0, constants.HEIGHT):
            pos = Position(x,y)

            if game_map[pos].halite_amount >= 500:

                adjacent_positions = check_adjacent(game_map,x,y,1)
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
    Position,
    Position
]
"""
def check_adjacent(game_map,x,y,radius):
    adjacent_positions=[]
    for row in range(-radius, radius):
        for col in range(-radius, radius):
            pos = Position(x,y).directional_offset(row,col)
            adjacent_positions.append(pos)

    return adjacent_positions


"""
Return:
[
    [Position, halite_amount],
    [Position, halite_amount]
]
"""
def check_adjacent_halite(game_map,x,y,radius):
    adj = check_adjacent(game_map,x,y,radius)
    halite=[]
    for pos in adj:
        halite.append( [ pos, game_map[pos].halite_amount ] )

    return halite

"""
Return:
    Number of enemies within radius of x,y position.
"""
def check_adjacent_enemies(game_map,x,y,radius):
    adj = check_adjacent(game_map,x,y,radius)
    num_enemies = 0
    for pos in adj:
        if pos.ship.owner != game.me:
            num_enemies+=1
    return num_enemies


"""
Return:
[
    Position, amount
]
"""
def highest_adjacent(game_map,x,y):
    adjacent_positions = check_adjacent_halite(game_map,x,y,1)
    position = adjacent_positions[0][0]
    highest_halite = adjacent_positions[0][1];
    for pos in adjacent_positions:
        if pos[1] > highest:
            position = pos[0]
            highest = pos[1]

    return [position, highest]
