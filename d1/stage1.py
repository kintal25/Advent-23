def calc_row(row: str):
    digits = [int(c) for c in row if c.isdigit()]
    if len(digits) == 1:
        digits.append(digits[0])
    res = digits[0] * 10 + digits[-1]
    print(f"digits: {digits}, res: {res}")
    return res


def test():
    t = 'sdfssdfsdf2'
    print(calc_row(t))


def read_file(filename: str):
    with open(filename, 'r') as f:
        return f.readlines()


def run():
    inp = read_file('d1/input_1')
    sum = 0
    for i in inp:
        sum += calc_row(i)
    print(f"Result sum: {sum}")
