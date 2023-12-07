import utils


def get_races(inp: list) -> list:
    res = []
    times = [int(i) for i in inp[0].split(':')[1].split()]
    distances = [int(i) for i in inp[1].split(':')[1].split()]
    res = zip(times, distances)
    return res


def calc_race(race: tuple) -> int:
    wins = 0
    for t_hold in range(1, race[0]):
        dist = t_hold * (race[0] - t_hold)
        if dist > race[1]: wins += 1
    print(f"Race! Time: {race[0]}, distance: {race[1]}, wins: {wins}")        
    if wins == 0: return 1
    return wins


def test():
    t = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    a = 5


def run():
    FCHECK = 'input_check'
    FPROD = 'd6/input'
    inp = utils.read_file_lines(FPROD)
    res = 1
    for race in get_races(inp):
        res *= calc_race(race)

    print(f"\n====\nResult: {res}")
