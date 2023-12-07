import utils
from collections import Counter


def handle_line(row: str) -> tuple:
    cards = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 1,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    hand = [cards[i] for i in row.split()[0]]
    bid = int(row.split()[1])
    return (hand, bid)


def calc_power(hand: list, add_pow: int, real_jocker_hand: list=[]) -> int:
    power = 0
    if real_jocker_hand:
        return calc_power(real_jocker_hand, add_pow)
    
    for i, card in enumerate(hand[::-1]):        
        power += card * pow(15, i)
    return pow(15, add_pow) + power


def calc_hand_with_jocker(hand: list) -> int:
    if 1 not in hand:
        return calc_hand(hand)
    
    best_res = 0
    for i in range(2, 15):
        possible_hand = [i if x == 1 else x for x in hand]
        if calc_hand(possible_hand, hand) > best_res:
            best_res = calc_hand(possible_hand, hand)
    return best_res
        
    

def calc_hand(hand: list, real_jocker_hand: list=[]) -> int:
    """ Returns power of hand """    
    HAND_QTY = 5
    cards_qty = Counter(hand)
    cards_mc = cards_qty.most_common()
    if cards_mc[0][1] == 5:
        # five of a kind
        return calc_power(hand, HAND_QTY + 6, real_jocker_hand)   
    if cards_mc[0][1] == 4:
        # four of a kind
        return calc_power(hand, HAND_QTY + 5, real_jocker_hand)
    if cards_mc[0][1] == 3: 
        if cards_mc[1][1] == 2:
        # full house
            return calc_power(hand, HAND_QTY + 4, real_jocker_hand)
        else:
        # three of a kind
            return calc_power(hand, HAND_QTY + 3, real_jocker_hand)
    if cards_mc[0][1] == 2: 
        if cards_mc[1][1] == 2:
            # two pairs
            return calc_power(hand, HAND_QTY + 2, real_jocker_hand)
        else:
            # one pair
            return calc_power(hand, HAND_QTY + 1, real_jocker_hand)
    # high card
    return calc_power(hand, HAND_QTY, real_jocker_hand)        


def test():
    t = "32748 765"
    aa = handle_line(0, t)[0][0]
    a = calc_hand([1,2,2,2,2])
    print(a)


def run():
    FCHECK = 'input_check'
    FPROD = 'd7/input'
    inp = utils.read_file_lines(FPROD)
    res = 0
    hands = {
        #hand_num: [(hand, bid), power]
    }

    for i, line in enumerate(inp):
        hand = handle_line(line)
        print(f"Hand: {hand}")
        hands[i] = [hand, calc_hand_with_jocker(hand[0])]
    print(f"Hands: {hands}")
    sorted_hands_no_by_power = [k for k, v in sorted(hands.items(), key=lambda item: item[1][1])]
    for i, hand_no in enumerate(sorted_hands_no_by_power):
        res += hands[hand_no][0][1] * (i + 1)

    print(f"\n====\nResult: {res}")
