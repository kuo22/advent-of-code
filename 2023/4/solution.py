import re
import math
from pathlib import Path
from collections import defaultdict

def scratchcards_points_total(file_name="input.txt"):
    file_path = Path(Path(__file__).parent.absolute(), file_name)
    f = open(file_path, 'r')
    
    total_points = 0

    for card in f:
        card_matches = scratchcard_matches(card)
        
        if card_matches > 0:
            total_points += math.pow(2, card_matches - 1)
    
    f.close()
    return total_points

def scratchcards_won(file_name="input.txt"):
    file_path = Path(Path(__file__).parent.absolute(), file_name)
    f = open(file_path, 'r')

    card_counts = defaultdict(int)
    id = 0
    for card in f:
        id += 1
        card_counts[id] += 1
        matches = scratchcard_matches(card)
        
        for i in range((id + 1), (id + 1 + matches)):
            card_counts[i] += card_counts[id]
    
    f.close()

    return sum(card_counts.values())

def scratchcard_matches(card):
    id, numbers = card.split(':')

    winning_nums, my_nums = numbers.split('|')

    winning_set = set([i for i in winning_nums.split(' ') if i])
    my_nums_list = [i.strip() for i in my_nums.split(' ') if i]

    matches = 0
    for num in my_nums_list:
        if num in winning_set:
            matches += 1

    return matches

print("Scratchcard points total:", scratchcards_points_total())
print("Scratchcards won:", scratchcards_won())
