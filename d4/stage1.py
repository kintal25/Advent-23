import utils


def handle_row(row: str):
    row = row.replace("  ", " ")
    win_nums = row.split(' | ')[0].split(':')[1].strip().split(' ')
    cur_nums = row.split(' | ')[1].strip().split(' ')
    win_qty, res = 0, 0
    for cur_num in cur_nums:
        if cur_num in win_nums:
            win_qty += 1
            continue
    res = 0 if win_qty == 0 else pow(2, win_qty - 1)
    print(f"ticket result: {res}")
    return res


def test():
    t = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    print(handle_row(t))
    a = 5


def run():
    FCHECK = 'input_check'
    FPROD = 'd4/input'
    res = 0
    inp = utils.read_file_lines(FPROD)
    for card in inp:
        res += handle_row(card)
        print(f"cum_sum: {res}")
    print(f"\n====\nResult sum: {res}")
