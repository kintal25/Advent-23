import utils


def get_seeds(first_line: str):
    return map(int, first_line.split(':')[1].split())


def get_maps(lines: list):
    map, maps = [], []
    for line in lines:
        if line == "\n" or line == "": continue
        if ":" in line:
            if map:
                maps.append(map)
                map = []
        else:
            map.append(line)
    maps.append(map)
    return maps


def use_map(mapp: list, seed: int) -> int:
    res = seed
    for map_line in mapp:
        dest_range, source_range, r = [int(i) for i in map_line.split()]
        if seed < source_range or seed > source_range + r:
            continue
        res = dest_range + (seed - source_range)
        break
    print(f"Map convertation: {seed} -> {res}")
    return res


def test():
    t = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    a = 5


def run():
    FCHECK = 'input_check'
    FPROD = 'd5/input'
    locations = []
    inp = utils.read_file_lines(FPROD)
    seeds = get_seeds(inp[0])
    maps = get_maps(inp[2:])
    for seed in seeds:
        seed_res = seed
        print(f"\nSeed: {seed}")
        for mapp in maps:
            seed_res = use_map(mapp, seed_res)
        locations.append(seed_res)
    print(f"\n====\nResult: {min(locations)}")
