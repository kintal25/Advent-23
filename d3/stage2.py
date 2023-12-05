import re


def is_num_adjace_part(part_pos: int, num_pos: int, attempt=1):
    INPUT_COLS = 140
    part_pos_mod = part_pos - INPUT_COLS
    if num_pos == part_pos_mod or num_pos == part_pos_mod - 1 or num_pos == part_pos_mod + 1:
        return True
    if attempt == 3:
        return False
    attempt += 1
    return is_num_adjace_part(part_pos + INPUT_COLS, num_pos, attempt)


def get_numbers(input: str):
    res = {
        # first_pos_of_number: number
    }
    matches = re.finditer(r'(\d+)', input)
    for match in matches:
        number = input[match.span()[0]:match.span()[1]]
        res[match.span()[0]] = number
    print(f"numbers: {res}\n")
    return res


def get_gear_cand_positions(input: str):
    res = []
    matches = re.finditer(r'[\*]', input)
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
    gear_cand_positions = get_gear_cand_positions(inp)
    res = 0
    # pos of numbers, which passed even 1 check
    gear_cand_with_nums = {
        # gear_candidate_pos: [number1, number2, number3]
    }
    for part_pos in gear_cand_positions:
        for num_first_pos, num in numbers.items():
            for num_pos in range(num_first_pos, num_first_pos + len(num)):
                if is_num_adjace_part(part_pos, num_pos):
                    #print(f"found gear_candidate: pos: {part_pos}, number: {v}")
                    gear_cand_with_nums.setdefault(part_pos, []).append(int(num))
                    break
    for pos, nums in gear_cand_with_nums.items():
        if len(nums) == 2:
            res += nums[0] * nums[1]
    print(f"\n====\nResult sum: {res}")
