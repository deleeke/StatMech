import pygame, sys, random
from pygame.locals import *
import math, os.path

# Solved visualization problem. However, it could be improved
# by creating a solution that alternated between displaying
# the hits and misses more frequently.

sf = 'stoneDataFile.txt'
mf = 'missesDataFile.txt'

#Truncate Datafile to trash old results
stoneFile = open(sf, 'w')
stoneFile.close()
missedFile = open(mf, 'w')
missedFile.close()


def UsrError(message):
    print message

def markov_pi(N, delta):
    x, y = 1.0, 1.0
    n_hits = 0
    stones = []
    misses = []
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
        if x**2 + y**2 < 1.0:
            n_hits += 1
            #Transform x and y coordinates to be valid coordinates for the pygame window
            coordinates = '%d, %d\n' % ((x*200.000000 +195),(y*200.000000+195))
            stones.append(coordinates)
        else:
            missedcoords = '%d, %d\n' % ((x*200.000000 +195),(y*200.000000+195))
            misses.append(missedcoords)

    #store coordinates in external files
    stoneFile = open(sf, 'a')
    stoneFile.writelines(stones)
    stoneFile.close()
    missedFile = open(mf, 'a')
    missedFile.writelines(misses)
    missedFile.close()

    return n_hits

def run_the_trials(n_runs, n_trials):
    delta = 0.1
    for run in range(n_runs):
        result = 4.0 * markov_pi(n_trials, delta) / float(n_trials)
        if run % 100 == 0 and run != 0:
            print 'Run %d' % run
            print result
    print 'Markov chain Monte Carlo Results: %.6f' % result

def visualization(stoneData, missesData):
     #set up pygame
     pygame.init()
     mainClock = pygame.time.Clock()

     # set up window
     WINDOWWIDTH = 400
     WINDOWHEIGHT = 400
     windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
     pygame.display.set_caption('Markov Monte Carlo')

     # set up colors
     BLACK = (0, 0, 0)
     GREEN = (50, 200, 0)
     STONECOLOR = (45, 33, 100)
     MISSSTONECOLOR = (100, 0, 0)


     STONESIZE = 5
     stoneCoords = []

     MISSEDSTONESIZE = 5
     missedCoords = []

     stoneFile = open(stoneData, 'r')
     stoneFile = stoneFile.read()
     stones = stoneFile.split('\n')
     del(stones[-1])
     for i in range(len(stones)):
         stones[i] = stones[i].strip().replace(' ', '').split(',')
         stones[i][0] = int(stones[i][0])
         stones[i][1] = int(stones[i][1])

     for i in range(len(stones)):
         stoneCoords.append(pygame.Rect(stones[i][0], stones[i][1], STONESIZE, STONESIZE))

     missedFile = open(missesData, 'r')
     missedFile = missedFile.read()
     misses = missedFile.split('\n')
     del(misses[-1])
     for i in range(len(misses)):
         misses[i] = misses[i].strip().replace(' ', '').split(',')
         misses[i][0] = int(misses[i][0])
         misses[i][1] = int(misses[i][1])

     for i in range(len(misses)):
         missedCoords.append(pygame.Rect(misses[i][0], misses[i][1], MISSEDSTONESIZE, MISSEDSTONESIZE))

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

         for i in range(len(stoneCoords)):
             #draw the 'stones'
             pygame.draw.rect(windowSurface, STONECOLOR, stoneCoords[i])
             pygame.display.update()
         for i in range(len(missedCoords)):
             #draw the 'missed stones'
             pygame.draw.rect(windowSurface, MISSSTONECOLOR, missedCoords[i])
             pygame.display.update()

# Run the program

runs = 0
trials = 4000

while runs == 0:
    # run the simulation
    try:
        message = "How many runs of trials of %d iterations do you want to run? \n > " % trials
        runs = int(raw_input(message))
        run_the_trials(runs, trials)
        visualization(sf, mf)
    except ValueError:
        UsrError("Please enter an integer")
