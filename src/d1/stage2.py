def normalize_str(s: str):
    alphabet = {
        "oneight": 18,
        "twone": 21,
        "threeight": 38,
        "fiveight": 58,
        "sevenine": 79,
        "eightwo": 82,
        "eighthree": 83,
        "nineight": 98,
        ##
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    res = s

    for key, val in alphabet.items():
        if key in res:
            print(f"Replaced {key} to {val}")
        res = res.replace(key, str(val))
    return res


def calc_row(row: str):
    digits = [int(c) for c in row if c.isdigit()]
    if len(digits) == 1:
        digits.append(digits[0])
    res = digits[0] * 10 + digits[-1]
    print(f"normalize: {row}, digits: {digits}, res: {res}")
    return res


def test():
    t = 'xtwone3four'
    print(normalize_str(t))


def read_file(filename: str):
    with open(filename, 'r') as f:
        return f.readlines()


def run():
    FCHECK = 'input_check'
    FPROD = 'd1/input_2'
    inp = read_file(FPROD)
    sum = 0
    for i in inp:
        print(f"input: {i}")
        sum += calc_row(normalize_str(i))
        print(f"cum_sum: {sum}\n==\n")
    print(f"Result sum: {sum}")
