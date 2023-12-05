import utils


def handle_card(card: str):
    card = card.replace("  ", " ")
    win_nums = card.split(' | ')[0].split(':')[1].strip().split(' ')
    cur_nums = card.split(' | ')[1].strip().split(' ')
    win_qty = 0
    for cur_num in cur_nums:
        if cur_num in win_nums:
            win_qty += 1
            continue
    #print(f"ticket result: {res}")
    return win_qty


def test():
    t = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    print(handle_card(t))
    a = 5


def run():
    FCHECK = 'input_check'
    FPROD = 'd4/input'
    res = 0
    cards = {
        # card_no: qty
    }
    inp = utils.read_file_lines(FPROD)
    for i in range(len(inp)):
        cards[i + 1] = 1
    for i, card in enumerate(inp):
        card_no = i + 1
        win_qty = handle_card(card)
        card_qty = cards[card_no]
        for ii in range(card_no + 1, card_no + 1 + win_qty):
            cards[ii] = cards[ii] + card_qty  
        #print(f"Card {card_no}, win_qty: {win_qty}, this_card_qty: {card_qty}\nCards: {cards}\n")
    for card_no, card_qty in cards.items():
        res += card_qty
    print(f"Cards: {cards}\n====\nResult: {res}")
