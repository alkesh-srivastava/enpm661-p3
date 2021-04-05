# -*- coding: utf-8 -*-
import pygame
from configuration import return_path, move_possible
from priority_queue import PriorityQueue
import math, cv2
from map_creator import create_main_map
from matplotlib import pyplot as plt
from real_timeviz import a_star
# Declaration of Puzzle as blank spaces of 400x400 pixels :
puzzle = [[''] * 400] * 300


# Step 0 :


print("Note: Value of \u03F4 should only be in degrees (\N{DEGREE SIGN})\n"
      "Please Enter the starting co-ordinates of the robot and its orientation as (x,y,\u03F4):")
starting_coordinates = input()
start = starting_coordinates.split(',')
start = (int(start[0]), int(start[1]), int(start[2]))
print("Please Enter the goal co-ordinates of the robot and its orientation as (goal_x,goal_y,goal_\u03F4):")
goal_coordinates = input()
goal = goal_coordinates.split(',')
goal = (int(goal[0]), int(goal[1]), int(goal[2]))

# Clearance and robot radius :
print("Please Enter the radius of your Robot:")
bot_radius = int(input())
print("Please Enter the desired clearance of your Robot:")
bot_clearance = int(input())
clearance = bot_radius + bot_clearance
# Step size of movement in units ( 1 <= d <=10)
print("Please Enter the desired step size of your Robot:")
bot_step_size = int(input())
if bot_step_size < 1 or bot_step_size > 10:
    print("ERROR! Please Enter the step-size valued between 1 and 10.")
    raise SystemExit()
goal_equation = lambda x, y: ((x - goal[0]) ** 2) + ((y - goal[1]) ** 2) - (1.5 * bot_step_size) ** 2


if not move_possible(puzzle, start, clearance):
    print("The start is on a obstacle. RETRY!!")
    raise SystemExit()

if not move_possible(puzzle, goal, clearance):
    print("The goal is on a obstacle. RETRY!!")
    raise SystemExit()

# Theta** (angle between consecutive actions);
print("OPTIONAL: Please Enter the desired angle between consecutive actions, if none please press the Enter key:")
theta = input()

if theta == '':
    theta_in = 30
else:
    theta_in = int(theta)


# Step 1 : Defining Action definition in mathematical form
def offsets_fn(theta, theta_in):
    tuple_2x = roundingpoint((bot_step_size * (math.cos(math.radians(theta + (2 * theta_in)))),
                              bot_step_size * (math.sin(math.radians(theta + (2 * theta_in))))))
    tuple_x = roundingpoint((bot_step_size * (math.cos(math.radians(theta + theta_in))),
                             bot_step_size * (math.sin(math.radians(theta + theta_in)))))
    tuple_0 = roundingpoint((bot_step_size * (math.cos(math.radians(theta))),
                             bot_step_size * (math.sin(math.radians(theta)))))
    tuple_n2x = roundingpoint((bot_step_size * (math.cos(math.radians(theta - (2 * theta_in)))),
                               bot_step_size * (math.sin(math.radians(theta - (2 * theta_in))))))
    tuple_nx = roundingpoint((bot_step_size * (math.cos(math.radians(theta - theta_in))),
                              bot_step_size * (math.sin(math.radians(theta - theta_in)))))

    offsets = {
        "2x_positive_theta": (tuple_2x[0], tuple_2x[1], 2* theta_in),
        "positive_theta": (tuple_x[0], tuple_x[1], theta_in),
        "zero": (tuple_0[0], tuple_0[1], 0),
        "negative_theta": (tuple_nx[0], tuple_nx[1], -theta_in),
        "2x_negative_theta": (tuple_n2x[0], tuple_n2x[1], -2* theta_in),
    }
    return offsets
# Step 2:
# Check Configuration file
a_star(puzzle, start, goal, clearance, bot_step_size, theta_in)
