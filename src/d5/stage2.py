import utils
import multiprocessing as mp
from multiprocessing import Pool
from itertools import product
from concurrent.futures import ProcessPoolExecutor


def get_seeds(first_line: str):
    res = []
    data = [int(i) for i in first_line.split(':')[1].split()]

    for s, r in zip(data[0::2], data[1::2]):
        res.extend(range(s, s + r))

    return res


def get_seeds_range(first_line: str):
    res = []
    data = [int(i) for i in first_line.split(':')[1].split()]

    for seed_min, r in zip(data[0::2], data[1::2]):
        res.append([seed_min, seed_min + r])

    return res


def get_maps(lines: list):
    map_obj, maps = [], []
    for line in lines:
        if line == "\n" or line == "": continue
        if ":" in line:
            if map_obj:
                maps.append(map_obj)
                map_obj = []
        else:
            dest_range, source_range, r = [int(i) for i in line.split()]
            map_obj.append((dest_range, source_range, r))
    maps.append(map_obj)
    return maps


def get_maps_range(lines: list):
    map_obj, maps = [], []
    for line in lines:
        if line == "\n" or line == "": continue
        if ":" in line:
            if map_obj:
                maps.append(map_obj)
                map_obj = []
        else:
            dest_range, source_range, r = [int(i) for i in line.split()]
            map_obj.extend([dest_range, dest_range + r, source_range, source_range + r])
    maps.append(map_obj)
    return maps    



def use_map(map_obj: list, seed: int) -> int:
    res = seed
    for map_line in map_obj:
        if seed < map_line[1] or seed > map_line[1] + map_line[2]:
            continue
        res = map_line[0] + (seed - map_line[1])
        break
    # print(f"Map convertation: {seed} -> {res}")
    return res


def use_map_range(map_obj: list, seed_min: int, seed_max: int) -> int:
    for map_line in map_obj:
        res_range = []
        seed_range = seed_max - seed_min
        map_out_min, map_out_max, map_in_min, map_in_max = map_line
        is_seed_in_mapline = True
        if seed_min >= map_in_min:
            if seed_max <= map_in_max:
                delta = seed_min - map_in_min
                res_range = (map_out_min + delta, map_out_min + delta + seed_range)
            elif seed_min < map_in_max and seed_max >= map_in_max
                new_in_ranges = [(seed_min, map_in_max - 1), (map_in_max, seed_max)]
        if seed_max < map_in_min or seed_min > map_in_max:
            is_seed_in_mapline = False
            continue
        if seed_min >= map_in_min and seed_max <= map_in_max:
            delta = seed_min - map_in_min
            res_range = (map_out_min + delta, map_out_min + delta + seed_range)
        elif seed_min >= map_in_min and seed_max > map_in_max:
            new_in_ranges = [(seed_min, map_in_max - 1), (map_in_max, seed_max)]
        elif seed_max <= map_in_max and seed_min < map_in_min            
            new_in_ranges = [(seed_min, map_in_min), (map_in_min + 1, seed_max)]
        # if seed_max > map_in_min:
        #     new_seed_ranges = [(map_in_min, seed_max)], ()]

        break
    # print(f"Map convertation: {seed} -> {res}")
    return res


def test():
    t = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    a = 5


def get_seeds_and_run(inp):
    locations = []
    maps = get_maps(inp[2:])

    data = [int(i) for i in inp[0].split(':')[1].split()]
    for s, r in zip(data[0::2], data[1::2]):
        for seed in range(s, s + r):
            for map_obj in maps:
                seed_res = use_map(map_obj, seed)
                locations.append(seed_res)
    
    print(f"res: {min(locations)}\n")  


def get_seeds_and_run_new(inp):
    locations = []
    maps = get_maps_range(inp[2:])

    data = [int(i) for i in inp[0].split(':')[1].split()]
    for s, r in zip(data[0::2], data[1::2]):
        for map_obj in maps:
            seed_res = use_map_range(map_obj, s, s + r)
            locations.append(seed_res)
    
    print(f"res: {min(locations)}\n")      


def use_map_parallel(s: int, r: int, maps:list):
    locations = []
    for seed in range(s, s + r):
        seed_res = seed
        for map_obj in maps:
            seed_res = use_map(map_obj, seed_res)
        locations.append(seed_res)
    # print(f"From seed {s}, range {r} locations: {locations}")
    return locations

def get_seeds_and_run_parallel(inp):
    PROC_NUM = mp.cpu_count()
    print(f"Number of cpu :{mp.cpu_count()}")
    maps = get_maps(inp[2:])
    
    args_parallel = []
    data = [int(i) for i in inp[0].split(':')[1].split()]
    for s, r in zip(data[0::2], data[1::2]):
        args_parallel.append((s, r, maps))
    
    with Pool(PROC_NUM) as p:
        locations = p.starmap(use_map_parallel, args_parallel)
    res = min(min(r) for r in locations)
    print(f"res: {res}\n")


def run():
    FCHECK = 'input_check'
    FPROD = 'd5/input'
    inp = utils.read_file_lines(FPROD)
    get_seeds_and_run(inp)
    # get_seeds_and_run_parallel2(inp)
