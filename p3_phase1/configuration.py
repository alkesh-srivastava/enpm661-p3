# This file is the main configuration file that defines the configuration of our maze.
# In this file, we will be declaring the possible move sets, defining obstacle and
# constraints that will restrict the motion of our player.


# Let us define movement offsets :

global_explore_x = list()  # I am not sure if I will be using it
global_explore_y = list()  # This either
offsets = {  # These are movement offsets, that define the motion of
    # the player grid by grid.
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
    "up-left": (-1, -1),
    "up-right": (-1, 1),
    "down-left": (1, -1),
    "down-right": (1, 1)
}

def obstacle(x, y, clearance = 15):  # This function definition inspects whether a coordinate point x
    # and y lie on the obstacle or not
    inside_circle = False
    inside_rectangle = False
    inside_ellipse = False
    inside_C1 = False
    inside_C2 = False
    inside_C3 = False

    if ((x - 90) ** 2 + (y - 70) ** 2) <= ((35+clearance) ** 2):  # Changed to 50 instead of 35
        inside_circle = True
    if (y >= 0.7 * x + 74.4 - clearance) and \
            (y >= -1.42 * x + 176.16 - clearance) and \
            (y <= -1.42 * x + 436.82 + clearance) and \
            (y <= 0.7 * x + 97.18 + clearance):  # Change the intercepts with -15 on the lower values and +15 on higher values
        inside_rectangle = True
    if ((x - 246) ** 2) / ((60+clearance) ** 2) + (y - 175) ** 2 / ((30+clearance) ** 2) <= 1:  # Changed 60 to 75 and 30 to 45
        inside_ellipse = True

    if 200 - clearance < x < 210 + clearance and 240 - clearance < y < 270 + clearance:  # -15 in lower limit and +15 in higher limit for
        # all the limits
        inside_C1 = True

    if 200 - clearance < x < 230 + clearance and 230 - clearance < y < 240 + clearance:
        inside_C2 = True

    if 200 - clearance < x < 230 + clearance and 270 - clearance < y < 280 + clearance:
        inside_C3 = True

    if inside_circle or inside_rectangle or inside_ellipse or inside_C1 or inside_C2 or inside_C3:
        return True
    else:
        return False


# I defined this function with the intent to store every move
# in a list, but I guess they will never be used
def all_moves(pos):
    x, y = pos
    global_explore_x.append(x)
    global_explore_y.append(y)


# This is the Bible of this project. This definition checks whether
# the move which is about to be performed by the player (Testudo)
# is possible or not. That is, if the move will result in a position
# that is either outside the maze boundaries or lie on an obstacle.

def move_possible(maze, pos):
    all_moves(pos)
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    if (0 <= i < num_rows and 0 <= j < num_cols and not (obstacle(i, j))):
        all_moves(pos)

    return 0 <= i < num_cols and 0 <= j < num_rows and not (obstacle(i, j))


# The function return_path is responsible for returning the possible moves
# that the player should perform to reach to its final stage.
# The function traces back its predecessors after it has reached a goal and
# then a reversed path will give the actual solution

def return_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path


if __name__ == "__main__":
    print("There is no point of running this file.")
