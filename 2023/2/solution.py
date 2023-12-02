import re
from functools import reduce
from pathlib import Path

def valid_game_sum(red, green, blue, file_name="input.txt"):
    file_path = Path(Path(__file__).parent.absolute(), file_name)
    f = open(file_path, 'r')
    
    sum = 0
    for game in f:
        if is_valid_game(game, red, green, blue):
           sum += game_id(game)

    return sum

def game_id(game):
    game_id_pattern = "Game (\d+)"
    id = re.search(game_id_pattern, game).group(1)

    return int(id)

def is_valid_game(game, red, green, blue):
    game_sets_pattern = "(?=: (.+))"
    sets = re.search(game_sets_pattern, game).group(1)

    set_list = sets.split(';')

    marble_amounts = {
        "red": red,
        "green": green,
        "blue": blue
    }
    for set in set_list:
        marbles = [s.strip() for s in set.split(',')]
        for marble in marbles:
            count, color = marble.split(' ')
            count = int(count)

            if count > marble_amounts[color]:
                return False
    
    return True


def game_power_sum(file_name="input.txt"):
    file_path = Path(Path(__file__).parent.absolute(), file_name)
    f = open(file_path, 'r')
    
    power_sum = 0
    for game in f:
        power_sum += game_power(game)

    return power_sum

def game_power(game):
    game_sets_pattern = "(?=: (.+))"
    sets = re.search(game_sets_pattern, game).group(1)

    set_list = sets.split(';')

    marble_min = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for set in set_list:
        marbles = [s.strip() for s in set.split(',')]
        for marble in marbles:
            count, color = marble.split(' ')
            count = int(count)

            if count > marble_min[color]:
                marble_min[color] = count
    
    return reduce(lambda a, b: a * b, marble_min.values())


red = 12
green = 13
blue = 14
print("Valid game sum:", valid_game_sum(12, 13, 14))            
print("Power sum:", game_power_sum())
