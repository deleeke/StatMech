import random
import sys

def UsrError(message):
    print message

def direct_pi(N):
    n_hits = 0
    for i in range(N):
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        if x ** 2 + y ** 2 < 1.0:
            n_hits += 1
    return n_hits

def run_the_trials(runs, trials):
    for run in range(runs):
        if (run % 100) == 0 and run > 0:
            print '%d runs: ' % run
            print 4.0 * direct_pi(trials) / float(trials)
    print 'Final average after %d runs of trials of %d iterations is:' % (n_runs, n_trials)
    print 4.0 * direct_pi(trials) / float(trials)
    sys.exit(0)

# run the simulation

n_runs = 0
n_trials = 5000

while n_runs == 0:
    try:
        message = "How many runs of trials of %d iterations do you want to run? \n > " % n_trials
        n_runs = int(raw_input(message))
        run_the_trials(n_runs, n_trials)
    except ValueError:
        UsrError("Please enter an integer")
