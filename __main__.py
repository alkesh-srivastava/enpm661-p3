# We will be using pygame to animate the path.
# We will be using Testudo as our player, #GoTerps!
# Remember, you will see that Testudo sometimes overlap
# the border of obstacle. To be honest, it would have been
# very difficult to let a point object explore the maze.
# Testudo is a 10x10 sprite and thus the overlap.
# You can cross check the path (It will be printed in the
# terminal)
import pygame, __astar__, __dijkstra__


WIDTH, HEIGHT = 500, 400 # 50 pixel padding on each side
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project 2 - Testudo on a Hunt!")
WHITE = (255, 255, 255) # RGB
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
FPS = 60    # 60 frame per second
TESTUDO = pygame.image.load('images/testudo.png')
TESTUDO_RESIZE = pygame.transform.scale(TESTUDO, (10, 10))
BACKGROUND = pygame.image.load('images/Path_1_1.png') # It was a hassle learning and drawing equations on pygame in the
                                                      # limited time period. I plotted the equations using matplotlib
                                                      # and saved it as an image
BACKGROUND = pygame.transform.scale(BACKGROUND, (401, 301))
# Offsets to compensate for our padding:
x_offset = 49
y_offset = 300
y_upper_offset = 50

global initial_testudo


def draw_window(rect):
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND, (50, 50))
    WIN.blit(TESTUDO_RESIZE, (rect.x, rect.y))
    pygame.draw.circle(WIN, GREEN, [x_offset + goal_x, (y_offset - goal_y) + y_upper_offset], 10)
    pygame.draw.rect(WIN, BLACK, (50, 50, 400, 300), 3)

    pygame.display.update()


def main():
    player = pygame.Rect(x_offset, y_offset + y_upper_offset, 0, 0)

    clock = pygame.time.Clock()
    run = True
    counter = 0
    while run:
        try:
            clock.tick(FPS)
            # print(solution[counter])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            if counter == 0:
                player.x += solution[counter][0]
                player.y -= solution[counter][1]

            if counter > 1:
                player.x += (solution[counter][0] - solution[counter - 1][0])
                player.y -= (solution[counter][1] - solution[counter - 1][1])
            draw_window(player)
            counter = counter + 1
            if counter > counter_stop:
                pygame.time.wait(0)


        except:


            run = False
            pygame.quit()

    pygame.quit()


if __name__ == '__main__':
    print("Input Start Position for Testudo :\nX Co-ordinate :")
    testudo_x = int(input())
    if testudo_x > 400 or testudo_x < 0:
        print("Your input contains an obstacle or there was an invalid entry.\nPLEASE RESTART THE PROGRAM!")
        raise SystemExit()
    print("Y Co-ordinate :")
    testudo_y = int(input())
    if testudo_y > 300 or testudo_x < 0:
        print("Your input contains an obstacle or there was an invalid entry.\nPLEASE RESTART THE PROGRAM!")
        raise SystemExit()
    print("Input Goal Position for Testudo :\nX Co-ordinate :")
    goal_x = int(input())
    if goal_x > 400 or goal_x < 0:
        print("Your input contains an obstacle or there was an invalid entry.\nPLEASE RESTART THE PROGRAM!")
        raise SystemExit()
    print("Y Co-ordinate :")
    goal_y = int(input())

    if goal_y > 300 or goal_y < 0:
        print("Your input contains an obstacle or there was an invalid entry.\nPLEASE RESTART THE PROGRAM!")
        raise SystemExit()
    print("Use your preferred method:\nPress 1 for Dijkstra.\nPress 2 for A*")

    _method = int(input())


    puzzle = [[''] * 400] * 300
    if _method == 1:
        solution = __astar__.a_star(puzzle, (testudo_x, testudo_y), (goal_x, goal_y))
    if _method == 2:
        solution = __dijkstra__.dijkstra(puzzle, (testudo_x, testudo_y), (goal_x, goal_y))
    counter_stop = len(solution)
    testudo_pos_x = x_offset + testudo_x
    testudo_pos_y = (y_offset - testudo_y) + y_upper_offset
    initial_testudo = (testudo_pos_x, testudo_pos_y)

    print("Path:\n" + str(solution))
    main()
    try:
        if _method == 1:
            solution = __astar__.a_star(puzzle, (testudo_x, testudo_y), (goal_x, goal_y))
        if _method == 2:
            solution = __dijkstra__.dijkstra(puzzle, (testudo_x, testudo_y), (goal_x, goal_y))
        counter_stop = len(solution)
        testudo_pos_x = x_offset + testudo_x
        testudo_pos_y = (y_offset - testudo_y) + y_upper_offset
        initial_testudo = (testudo_pos_x, testudo_pos_y)

        print("Path:\n"+str(solution))
        main()
    except:
        print("Your input contains an obstacle or there was an invalid entry.\nPLEASE RESTART THE PROGRAM!")
        raise SystemExit()