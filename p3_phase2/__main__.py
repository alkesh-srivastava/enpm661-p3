# -*- coding: utf-8 -*-
import math
from configuration import return_path, move_possible
from priority_queue import PriorityQueue
import math
from matplotlib import pyplot as plt


# Definition
def roundingpoint(point):
    if point[0].is_integer() and point[1].is_integer() or (point[0] - 0.5).is_integer() and (
            point[1] - 0.5).is_integer():
        return point
    else:
        new_point = (round(point[0] * 2) / 2, round(point[1] * 2) / 2)
        return new_point


def visualization(visited_nodes, path):
    fig, ax = plt.subplots()
    i = 0
    while True:
        ax.quiver(visited_nodes[i][0], visited_nodes[i][1], visited_nodes[i][0] - visited_nodes[i + 1][0],
                  visited_nodes[i][1] - visited_nodes[i + 1][1], units='xy', scale = 2)
        i += 1
        if i == (len(visited_nodes) - 1):
            break
        plt.xlim((0, 400))
        plt.ylim((0, 300))

    i = 0
    while True:
        ax.quiver(path[i][0], path[i][1], path[i][0] - path[i + 1][0],
                  path[i][1] - path[i + 1][1], units='xy', color='r', scale = 2)
        i += 1
        if i == (len(path) - 1):
            break
    plt.show()


##############################################


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
# Step size of movement in units ( 1 <= d <=10)
print("Please Enter the desired step size of your Robot:")
bot_step_size = int(input())
if bot_step_size < 1 or bot_step_size > 10:
    print("ERROR! Please Enter the step-size valued between 1 and 10.")
    raise SystemExit()
goal_equation = lambda x, y: ((x - goal[0]) ** 2) + ((y - goal[1]) ** 2) - (1.5 * bot_step_size) ** 2

# Theta** (angle between consecutive actions);
print("OPTIONAL: Please Enter the desired angle between consecutive actions, if none please press the Enter key:")
theta = input()

if theta == '':
    theta = 30
else:
    theta = int(theta)

# Step 1) Define the actions in a mathematical format
tuple_2x = roundingpoint((bot_step_size * (math.cos(math.radians(2 * theta))),
                          bot_step_size * (math.sin(math.radians(2 * theta)))))
tuple_x = roundingpoint((bot_step_size * (math.cos(math.radians(theta))),
                         bot_step_size * (math.sin(math.radians(theta)))))
tuple_n2x = roundingpoint((bot_step_size * (math.cos(math.radians(-2 * theta))),
                           bot_step_size * (math.sin(math.radians(-2 * theta)))))
tuple_nx = roundingpoint((bot_step_size * (math.cos(math.radians(-1 * theta))),
                          bot_step_size * (math.sin(math.radians(-1 * theta)))))

offsets = {
    "2x_positive_theta": (tuple_2x[0], tuple_2x[1], theta),
    "positive_theta": (tuple_x[0], tuple_x[1], theta),
    "zero": (bot_step_size, 0, theta),
    "negative_theta": (tuple_nx[0], tuple_nx[1], theta),
    "2x_negative_theta": (tuple_n2x[0], tuple_n2x[1], theta),
}


# Step 2:
# Check Configuration file

# Step 3:

def heuristic(a, b):
    # Euclidean Distance
    x1, y1, z1 = a
    x2, y2, z2 = b
    return abs(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


def a_star(maze, start, goal):
    pq = PriorityQueue()
    pq.put(start, 0)
    predecessors = {start: None}
    g_values = {start: 0}
    coordinates = list()

    while not pq.is_empty():
        current_cell = pq.get()
        # and current_cell[2] == goal[2]
        if goal_equation(current_cell[0], current_cell[1]) < 0:
            return return_path(predecessors, start, current_cell), coordinates

        for direction in ["2x_positive_theta", "positive_theta", "zero", "negative_theta", "2x_negative_theta"]:
            row_offset, col_offset, orientation = offsets[direction]
            if current_cell[2] + orientation < 360:
                neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset, current_cell[2] + orientation)
            elif current_cell[2] + orientation > 360:
                neighbour = (
                current_cell[0] + row_offset, current_cell[1] + col_offset, current_cell[2] + orientation - 360)
            elif current_cell[2] + orientation == 360:
                neighbour = (
                    current_cell[0] + row_offset, current_cell[1] + col_offset, 0)
            print("Neighbor:", neighbour)
            if move_possible(maze, neighbour) and neighbour not in g_values:
                new_cost = g_values[current_cell] + 1  # Uniform Step Cost
                g_values[neighbour] = new_cost
                f_value = new_cost + heuristic(goal, neighbour)
                pq.put(neighbour, f_value)
                predecessors[neighbour] = current_cell
                coordinates.append(neighbour)

    return None


# Execution


try:
    puzzle = [[''] * 400] * 300
    solution, explored_path = a_star(puzzle, start, goal)
    # visualization(explored_path, solution)

except:
    print("Something is wrong with your input!")
