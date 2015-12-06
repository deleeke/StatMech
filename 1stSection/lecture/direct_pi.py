import random
import sys
import os.path


def run_the_trials():
    n_trials = 0
    while n_trials == 0:
        try:
            n_trials = int(raw_input("How many trials do you want to run? \n> "))
        except ValueError:
            UsrError("Please enter an integer")
    filename = '1_lecture/direct_pi_results.txt'
    f = open(filename, 'w')
    n_hits = 0
    results = []
    for trial in range(n_trials):
        if (trial % 1000) == 0:
            print '%d trials, the average is now:' % trial
            print 4.0 * n_hits / float(n_trials)
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        if x ** 2 + y ** 2 < 1.0:
            n_hits += 1
            results.append(n_hits / float(n_trials))
    print 'After %d trials, the final average is:' % n_trials
    print 4.0 * n_hits / float(n_trials)
    f.write(str(results))
    sys.exit(0)


def UsrError(message):
    print message
    run_the_trials()

#run the program
run_the_trials()
