import utils


def get_history_line(inp_row: str) -> list[int]:
    return [int(i) for i in inp_row.split()]


def calc_dif_line(val: list[int]) -> list[int]:
    res = []
    for i, num in enumerate(val):
        if i == 0: continue
        res.append(num - val[i - 1])
    return res


def calc_diffs(hist: list[int]) -> list(list[int]):
    res = []
    dif = hist
    while not all(i == 0 for i in dif):
        dif = calc_dif_line(dif)
        res.append(dif)
    return res


def calc_predict(diffs: list[list[int]]) -> int:
    predict = 0
    for dif in reversed(diffs[:-1]):
        predict = dif[0] - predict
    return predict
        

def test():
    t = "32748 765"
    print(t)


def run():
    FCHECK = 'input_check'
    FPROD = 'd9/input'
    inp = utils.read_file_lines(FPROD)
    res = 0
    for row in inp:
        hist = get_history_line(row)
        diffs = calc_diffs(hist)
        diffs.insert(0, hist)
        predict = calc_predict(diffs)
        res += predict
        print(f"Row: {row}, predict: {predict}")

    print(f"\n====\nResult: {res}")
