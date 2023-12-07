import re
from pathlib import Path
from collections import defaultdict
from functools import cmp_to_key

def total_winnings(file_name="input.txt"):
    file_path = Path(Path(__file__).parent.absolute(), file_name)
    f = open(file_path, 'r')
    
    hand_bids = {}
    hands = []
    for line in f:
        hand, bid = line.strip().split()
        bid = int(bid)
        hand_bids[hand] = bid
        hands.append(hand)

    hands.sort(key=cmp_to_key(compare))
    total_winnings = 0
    for i, hand in enumerate(hands):
        total_winnings += hand_bids[hand] * (i + 1)
    
    return total_winnings

def total_winnings_with_jokers(file_name="input.txt"):
    file_path = Path(Path(__file__).parent.absolute(), file_name)
    f = open(file_path, 'r')
    
    hand_bids = {}
    hands = []
    for line in f:
        hand, bid = line.strip().split()
        bid = int(bid)
        hand_bids[hand] = bid
        hands.append(hand)

    hands.sort(key=cmp_to_key(compare_with_jokers))
    total_winnings = 0
    for i, hand in enumerate(hands):
        total_winnings += hand_bids[hand] * (i + 1)
    
    return total_winnings

def compare(hand1, hand2):
    type1 = hand_type(hand1)
    type2 = hand_type(hand2)

    if type1 != type2: return type1 - type2

    card_strength = {
        "A": 20,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }
    
    for i in range(0, 5):
        if hand1[i] != hand2[i]:
            return card_strength[hand1[i]] - card_strength[hand2[i]]
    
    return 0

def compare_with_jokers(hand1, hand2):
    type1 = hand_type_with_jokers(hand1)
    type2 = hand_type_with_jokers(hand2)

    if type1 != type2: return type1 - type2

    card_strength = {
        "A": 20,
        "K": 13,
        "Q": 12,
        "J": 0,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }
    
    for i in range(0, 5):
        if hand1[i] != hand2[i]:
            return card_strength[hand1[i]] - card_strength[hand2[i]]
    
    return 0

def hand_type(hand):
    counts = defaultdict(int)
    
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6

    for card in hand:
        counts[card] += 1

    if len(counts) == 1: return FIVE_OF_A_KIND
    if len(counts) == 2:
        if 4 in counts.values():
            return FOUR_OF_A_KIND
        else:
            return FULL_HOUSE
    if len(counts) == 3:
        if 3 in counts.values():
            return THREE_OF_A_KIND
        else:
            return TWO_PAIR
    if len(counts) == 4:
        return ONE_PAIR
    else:
        return HIGH_CARD

def hand_type_with_jokers(hand):
    counts = defaultdict(int)
    
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6

    for card in hand:
        counts[card] += 1
    
    j_count = counts.pop("J", 0)
    if j_count == 5:
        counts["J"] = 5
    else:
        most_common_card = max(counts, key=counts.get)
        counts[most_common_card] += j_count

    if len(counts) == 1: return FIVE_OF_A_KIND
    if len(counts) == 2:
        if 4 in counts.values():
            return FOUR_OF_A_KIND
        else:
            return FULL_HOUSE
    if len(counts) == 3:
        if 3 in counts.values():
            return THREE_OF_A_KIND
        else:
            return TWO_PAIR
    if len(counts) == 4:
        return ONE_PAIR
    else:
        return HIGH_CARD

print("Total winnings:", total_winnings())
print("Total winnings with joker:", total_winnings_with_jokers())
