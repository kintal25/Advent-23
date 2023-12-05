import re


def is_part_number(part_pos: int, check_pos: int, attempt=1):
    INPUT_COLS = 140
    part_pos_mod = part_pos - INPUT_COLS
    if check_pos == part_pos_mod or check_pos == part_pos_mod - 1 or check_pos == part_pos_mod + 1:
        return True
    if attempt == 3:
        return False
    attempt += 1
    return is_part_number(part_pos + INPUT_COLS, check_pos, attempt)


def get_numbers(input: str):
    res = {}
    matches = re.finditer(r'(\d+)', input)
    for i in matches:
        number = input[i.span()[0]:i.span()[1]]
        res[i.span()[0]] = number
        # for j in range(i.span()[0], i.span()[1]):
        #     res[j] = number
        #     a = 5
    print(f"numbers: {res}\n")
    return res


def get_part_positions(input: str):
    res = []
    matches = re.finditer(r'[^\d\w\.]', input)
    for match in matches:
        res.append(match.span()[0])
        print(f"found part: {match[0]}, pos: {match.span()[0]}")
    print(f"part_positions: {res}")
    return res


def read_file(filename: str):
    with open(filename, 'r') as f:
        return f.read()


def test():
    t = "467..114.....*........35..633.......#...617*...........+.58...592...........755....$.*.....664.598.."
    #get_numbers_re(t)
    a = 5


def run():
    FCHECK = 'input_check'
    FPROD = 'd3/input'
    inp = read_file(FPROD).replace("\n", "")
    numbers = get_numbers(inp)
    part_positions = get_part_positions(inp)
    res = 0
    for part_pos in part_positions:
        for k, v in numbers.items():
            for i in range(k, k + len(numbers[k])):
                if is_part_number(part_pos, i):
                    #print(f"found part_number: {numbers[k]}, cum_sum: {res}")
                    res += int(numbers[k])
                    break
    print(f"\n====\nResult sum: {res}")
