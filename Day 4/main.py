class Card:
    def __init__(self, id, winning_nums, own_numbs) -> None:
        self.id = id
        self.winning_nums = winning_nums
        self.own_nums = own_numbs
        self.next = None
    
    def set_next(self, next):
        self.next = next


with open("Day 4/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

head = None
prev = None
for line in lines:
    card_num, (winning_nums, own_nums) = int(line.split(": ")[0].replace("Card ", "")), line.split(": ")[1].split(" | ")
    winning_nums = [int(x) for x in winning_nums.split(" ") if len(x)]
    own_nums = [int(x) for x in own_nums.split(" ") if len(x)]
    card = Card(card_num, winning_nums, own_nums)

    if head == None:
        head = card
    else:
        prev.set_next(card)
    
    prev = card

total = 1
def count_cards(card):
    global total
    total += 1
    amount = sum([1 for own_num in card.own_nums if own_num in card.winning_nums])
    for _ in range(amount):
        card = card.next
        count_cards(card)


def part_one():
    total = 0
    card = head
    while (card.next != None):
        total += int(2 ** (sum([1 for own_num in card.own_nums if own_num in card.winning_nums]) - 1))
        card = card.next
    return total

def part_two():
    card = head
    while (card.next != None):
        count_cards(card)
        card = card.next
    return total


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")