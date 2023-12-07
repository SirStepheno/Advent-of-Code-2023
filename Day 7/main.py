import itertools
from functools import cmp_to_key

with open("Day 7/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

cards_seq = []

def get_rank(hand, joker=False):
    if joker:
        combinations = itertools.combinations_with_replacement(cards_seq, hand.count("J"))
        hands = [hand.replace("J", "") + "".join(combination) for combination in list(combinations)]
    else:
        hands = [hand]
    
    ranks = []
    for hand in hands:
        # Check for five of a kind
        if [card for card in cards_seq if hand.count(card) == 5]:
            ranks.append(6)
        # Check for four of a kind
        elif [card for card in cards_seq if hand.count(card) == 4]:
            ranks.append(5)
        # Check for full house
        elif [card for card in cards_seq if hand.count(card) == 3] and [1 for card in cards_seq if hand.count(card) == 2]:
            ranks.append(4)
        # Check for three of a kind
        elif [card for card in cards_seq if hand.count(card) == 3]:
            ranks.append(3)
        # Check for two pair
        elif len([card for card in cards_seq if hand.count(card) == 2]) == 2:
            ranks.append(2)
        # Check for one pair
        elif len([card for card in cards_seq if hand.count(card) == 2]) == 1:
            ranks.append(1)
        else:
            ranks.append(0)
    
    return max(ranks)

def check_order(hand1, hand2, i = 0):
    if hand1[i] == hand2[i]:
        return check_order(hand1, hand2, i + 1)
    elif cards_seq.index(hand1[i]) > cards_seq.index(hand2[i]):
        return 1
    return -1

def part_one():
    global cards_seq
    cards_seq = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

    all_hands = [[] for _ in range(7)]
    for line in lines:
        hand, strength = line.split(" ")
        all_hands[get_rank(hand)].append((hand, int(strength)))

    sorted_all_hands = [item for rank in all_hands for item in sorted(rank, key=cmp_to_key(lambda x, y:check_order(x[0], y[0])))]
    return sum([item[1] * i for i, item in enumerate(sorted_all_hands, start=1)])

def part_two():
    global cards_seq
    cards_seq = ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]

    all_hands = [[] for _ in range(7)]
    for line in lines:
        hand, strength = line.split(" ")
        all_hands[get_rank(hand, joker=True)].append((hand, int(strength)))

    sorted_all_hands = [item for rank in all_hands for item in sorted(rank, key=cmp_to_key(lambda x, y:check_order(x[0], y[0])))]
    return sum([item[1] * i for i, item in enumerate(sorted_all_hands, start=1)])

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))