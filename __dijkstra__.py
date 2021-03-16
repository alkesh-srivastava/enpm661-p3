from configuration import return_path, offsets, move_possible
from priority_queue import PriorityQueue
import math



def dijkstra(maze, start, goal):
    pq = PriorityQueue()
    pq.put(start, 0)
    predecessors = {start: None}
    g_values = {start: 0}

    while not pq.is_empty():
        current_cell = pq.get()
        if current_cell == goal:
            return return_path(predecessors, start, goal)

        for direction in ["up", "right", "down", "left", "up-left", "up-right", "down-left", "down-right"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if move_possible(maze, neighbour) and neighbour not in g_values:
                if direction == "up" or direction == "right" or direction == "down" or direction == "left":
                    new_cost = g_values[current_cell] + 1
                else:
                    new_cost = g_values[current_cell] + math.sqrt(2)
                g_values[neighbour] = new_cost
                f_value = new_cost + 0 # Denoting that Dijkstra can be considered a special case
                                       # of A star where Hueristic Function = 0
                pq.put(neighbour, f_value)
                predecessors[neighbour] = current_cell
    return None
