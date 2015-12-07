import pygame, sys, random
from pygame.locals import *
import math

# Currently this draws the circle
# And correctly makes the calculation
# But I've yet to re-engineer it to
# Assign appropriate x,y values to a "stone"
# And draw that on the screen
# The two main obstacles being, the feild is 200 X 200
# As far as pygame is concerned
# and the hypothetical square the calculation is randomly
# calling points inside of is 1 X 1.
# These two concerns being
# 1) How to
#      A) Change the algorithm so that it's x, y are the same as the "stone"
#      or
#      B) Transform the x, y value to an appropriate coordinate for the "stone"
#
# 2) How do the coordinates for our calculation relate to coordinates as
# far as pygame understands them


#set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

# set up colors
BLACK = (0, 0, 0)
GREEN = (50, 200, 0)
STONECOLOR = (45, 33, 100)

# set up the block data structure
stones = []

def UsrError(message):
    print message

def markov_pi(N, delta):
    x, y = 1.0, 1.0
    n_hits = 0
    stone_counter = 0
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
        if x**2 + y**2 < 1.0:
            n_hits += 1
            # for i in range(0, n_hits):
            #     if i % 1000 == 0:
            #         stones.append(pygame.Rect(x, y, 20, 20))
            #         pygame.draw.rect(windowSurface, STONECOLOR, stones[i])
            #         pygame.display.update()
    return n_hits

def simulation(n_runs, n_trials):
    delta = 0.1
    for run in range(n_runs):
        result = float(4.0 * markov_pi(n_trials, delta) / float(n_trials))
        pygame.display.set_caption('Markov chain Monte Carlo: %.6f' % result)

        if run % 100 == 0 and run != 0:
            print 'Run %d' % run
            accuracy = (float(4.0 * markov_pi(n_trials, delta) / float(n_trials)) % math.pi)
            #define the circle's thickness by how accurate we are getting
            # fill = int(200 - (round(200*accuracy)))
            # pygame.draw.circle(windowSurface, GREEN, (200, 200), 200, fill)
            # pygame.display.update()

    # the following code is to convert back to commandline UI
    #         if run % 1000 == 0 and run != 0:
    #         print 'Result from %d runs of %d trials each: ' % (run, n_trials)
    #         print 4.0 * markov_pi(n_trials, delta) / float(n_trials)
    #
    # print 'Final result from %d runs of %d trials each: ' % (run, n_trials)
    # print 4.0 * markov_pi(n_trials, delta) / float(n_trials)

runs = 0
trials = 4000

# draw the black background onto the surface
windowSurface.fill(BLACK)
pygame.draw.circle(windowSurface, GREEN, (200, 200), 200, 10)
pygame.display.update()

while True:
    # run the game loop
    #check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

    while runs == 0:
        # run the simulation
        try:
            message = "How many runs of trials of %d iterations do you want to run? \n > " % trials
            runs = int(raw_input(message))
            simulation(runs, trials)
            sys.exit(0)
        except ValueError:
            UsrError("Please enter an integer")
