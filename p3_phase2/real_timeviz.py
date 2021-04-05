import cv2
import math
import pygame
from configuration import return_path, move_possible
from map_creator import create_main_map
from priority_queue import PriorityQueue


def cv2_viz(visited_nodes, path, clearance):
    canvas = cv2.imread("Map.png")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    name = str(path[0]) + 'to' + str(path[-1]) + '.avi'
    print(name)
    out = cv2.VideoWriter(name, fourcc, 10, (canvas.shape[1], canvas.shape[0]))
    out.write(canvas)
    i = 0
    while True:
        cv2.arrowedLine(canvas, (int(visited_nodes[i][0]), 300 - int(visited_nodes[i][1])),
                        (int(visited_nodes[i + 1][0]), 300 - int(visited_nodes[i + 1][1])), (255, 0, 0), 1, cv2.LINE_AA)
        canvas = cv2.putText(canvas, "Robot Cearance : " + str(clearance) + " units", (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        out.write(canvas)
        i += 1
        if i == (len(visited_nodes) - 1):
            break
        cv2.imshow("Solution", canvas)
        cv2.waitKey(1)
    i = 0
    while True:
        cv2.arrowedLine(canvas, (int(path[i][0]), 300 - int(path[i][1])),
                        (int(path[i + 1][0]), 300 - int(path[i + 1][1])), (0, 0, 255), 1,
                        cv2.LINE_AA)
        out.write(canvas)
        i += 1
        if i == (len(path) - 1):
            break
        cv2.imshow("Solution", canvas)
        cv2.waitKey(1)

def heuristic(a, b):
    # Euclidean Distance
    x1, y1, z1 = a
    x2, y2, z2 = b
    return abs(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


def roundingpoint(point):
    # It rounds the floating point number to a float point of 1 significant figure after decimal.
    # e.g 67.7783568724862987469 to 67.5

    if point[0].is_integer() and point[1].is_integer() or (point[0] - 0.5).is_integer() and (
            point[1] - 0.5).is_integer():
        return point
    else:
        new_point = (round(point[0] * 2) / 2, round(point[1] * 2) / 2)
        return new_point


def offsets_fn(theta, bot_step_size, theta_in):
    # Mathematical Definition of action sets that takes care of input orientation as well
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

def a_star(maze, start, goal, clearence, bot_step_size, theta_in):

    map_of_maze, o_list = create_main_map()
    pygame.init()

    gameDisplay = pygame.display.set_mode((map_of_maze.shape[1], map_of_maze.shape[0]), pygame.SCALED)
    pygame.display.set_caption("Solution - Animation")

    white = (255, 255, 255)  # Background
    black = (0, 0, 0)  # Obstacle
    red = (255, 0, 0)  # Visited Node
    blue = (0, 0, 255)  # Path
    green = (0, 255, 0)  # Goal

    surface = pygame.surfarray.make_surface(map_of_maze)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('animation.avi', fourcc, 100, (
        map_of_maze.shape[1], map_of_maze.shape[0]))  # Increase the frame rate here(set to 750), for faster video

    gameDisplay.fill(white)

    clock = pygame.time.Clock()

    while True:
        for point in o_list:
            pygame.draw.rect(gameDisplay, black, [point[1], point[0], 1, 1])
        break

    pygame.draw.rect(gameDisplay, green, [goal[0], 300 - (goal[1]), 3, 3])
    pygame.image.save(gameDisplay, f"load.png")
    image = cv2.imread('load.png')
    cv2.imshow("Solution", image)
    cv2.waitKey(1)
    out.write(image)

    pq = PriorityQueue()
    pq.put(start, 0)
    predecessors = {start: None}
    g_values = {start: 0}
    coordinates = list()

    while not pq.is_empty():
        current_cell = pq.get()
        # and current_cell[2] == goal[2] ####### IMPORTANT FOR TAKING GOAL ORIENTATION AS CONSIDERATION
        if ((current_cell[0] - goal[0]) ** 2) + ((current_cell[1] - goal[1]) ** 2) - (1.5 * bot_step_size) ** 2 <= 0:
            path_list = return_path(predecessors, start, current_cell)
            break
        offsets = offsets_fn(current_cell[2], bot_step_size, theta_in)
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

            if move_possible(maze, neighbour, clearence) and neighbour not in g_values:
                new_cost = g_values[current_cell] + 1  # Uniform Step Cost
                g_values[neighbour] = new_cost
                f_value = new_cost + heuristic(goal, neighbour)
                pq.put(neighbour, f_value)
                predecessors[neighbour] = current_cell
                print("Neighbor:", neighbour)
                coordinates.append(neighbour)
                pygame.draw.rect(gameDisplay, red, [neighbour[0], 300 - neighbour[1], 1, 1])
                pygame.image.save(gameDisplay, f"load.png")
                image = cv2.imread('load.png')
                cv2.imshow("Solution", image)
                cv2.waitKey(1)
                out.write(image)

    for point in path_list:
        pygame.draw.rect(gameDisplay, blue, [point[0], 300 - (point[1]), 1, 1])
        pygame.image.save(gameDisplay, f"load.png")
        image = cv2.imread('load.png')
        cv2.imshow("Solution", image)
        cv2.waitKey(1)
        out.write(image)

    cv2_viz(coordinates, path_list, clearence)

    pygame.quit()
    return None
