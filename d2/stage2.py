def get_id(row: str):
    id = int(row.split(':')[0][len('Game '):])
    return id


def handle_row(row: str):
    rgb = {"red": 0, "green": 0, "blue": 0}
    attempts = row.split(':')[1].split(';')
    for attempt in attempts:
        handful = attempt.split(", ")
        for color_handful in handful:
            for k, v in rgb.items():
                if k not in color_handful:
                    continue
                qty = int(color_handful.replace(k, ''))
                if qty > rgb[k]:
                    rgb[k] = qty
    print(rgb)
    return rgb


def check_cond(rgb: dict):
    COND = {
        "red": 12, 
        "green": 13, 
        "blue": 14
    }
    res = all(COND[k] >= v for k, v in rgb.items())
    print(res)
    return res


def calc_power(rgb: dict):
    res = 1
    for k,v in rgb.items():
        res *= v
    print(f"calc_power: {res}")
    return res


def test():
    t = "Game 85: 5 green, 13 red, 11 blue; 5 blue, 19 green, 15 red; 17 red, 3 green, 8 blue; 13 green, 10 red; 3 green, 17 red, 11 blue"
    handle_row(t)


def read_file(filename: str):
    with open(filename, 'r') as f:
        return f.readlines()


def run():
    FCHECK = 'input_check'
    FPROD = 'd2/input_1'
    inp = read_file(FPROD)
    res = 0
    for i in inp:
        print(f"\n==\ninput: {i}")
        rgb = handle_row(i)
        res += calc_power(rgb)
        print(f"cum_sum: {res}")
    print(f"\n====\nResult sum: {res}")
