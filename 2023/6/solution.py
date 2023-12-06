import re
import math
from pathlib import Path
from collections import defaultdict

def winning_multiplier(file_name="input.txt"):
    file_path = Path(Path(__file__).parent.absolute(), file_name)
    f = open(file_path, 'r')

    time = [int(i) for i in f.readline().split()[1:]]
    distance = [int(i) for i in f.readline().split()[1:]]
    
    total = 1
    for i in range(0, len(time)):
        total *= ways_to_win_race(time[i], distance[i])

    return total

def long_race_winning_multiplier(file_name="input.txt"):
    file_path = Path(Path(__file__).parent.absolute(), file_name)
    f = open(file_path, 'r')

    time = int("".join(f.readline().split()[1:]))
    distance = int("".join(f.readline().split()[1:]))
    
    return ways_to_win_race(time, distance)


def ways_to_win_race(time, distance):
    a = -1
    b = time
    c = distance * -1

    discriminant = b**2 - 4 * a * c

    time1 = (time * -1 + math.sqrt(discriminant)) / (2 * a)
    time2 = (time * -1 - math.sqrt(discriminant)) / (2 * a)
      
    ways = math.floor(time2) - math.ceil(time1)

    if math.ceil(time1) > time2:
        return 0
    else:
        return ways + 1

print("Winning multiplier:", winning_multiplier())
print("Long race winning multiplier:", long_race_winning_multiplier()) 
