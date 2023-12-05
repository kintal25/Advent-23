import utils


def get_seeds(first_line: str):
    res = []
    data = [int(i) for i in first_line.split(':')[1].split()]
    #data = map(int, first_line.split(':')[1].split())

    for s, r in zip(data[0::2], data[1::2]):
        res.extend(range(s, s + r))

    return res


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


def use_map(map: list, seed: int) -> int:
    res = seed
    for map_line in map:
        dest_range, source_range, range = [int(i) for i in map_line.split()]
        if seed < source_range or seed > source_range + range:
            continue
        res = dest_range + (seed - source_range)
        break
    #print(f"Map convertation: {seed} -> {res}")
    return res


def test():
    t = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    a = 5


def get_seeds_and_run(inp):
    locations = []
    data = [int(i) for i in inp[0].split(':')[1].split()]
    maps = get_maps(inp[2:])
    
    for s, r in zip(data[0::2], data[1::2]):
        for seed in range(s, s + r):         
            seed_res = seed
            for map in maps:
                seed_res = use_map(map, seed_res)
            locations.append(seed_res)
            #print(f"Seed: {seed}, res:{seed_res}")
    print(f"\n====\nResult: {min(locations)}")


def run():
    FCHECK = 'input_check'
    FPROD = 'd5/input'
    locations = []
    inp = utils.read_file_lines(FPROD)
    get_seeds_and_run(inp)
    # seeds = get_seeds(inp[0])
    # print(f"Seeds: {seeds}")
    # maps = get_maps(inp[2:])
    # for seed in seeds:
    #     seed_res = seed
    #     print(f"\nSeed: {seed}")
    #     for map in maps:
    #         seed_res = use_map(map, seed_res)
    #     locations.append(seed_res)
    # print(f"\n====\nResult: {min(locations)}")
