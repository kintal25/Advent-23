import utils
from dataclasses import dataclass


MAZE_WIDTH = 140
MAZE_HEIGHT = 140


def get_data_doubled(inp: list[str]) -> list[tuple]:
    rows = []
    for i, line in enumerate(inp):
        rows.append(line)

        if all(x == '.' for x in line):
            print(f"Doubled row {i}")
            rows.append(line)
    
    cols = []
    for j in range(len(rows[0])):
        col = ''
        for i in range(len(rows)):
            col += rows[i][j]
        cols.append(col)            
        if all(x == '.' for x in col):
            print(f"Doubled column {j}")
            cols.append(col)
            
                
    galaxies = []
    for j in range(len(cols[0])):
        for i in range(len(cols)):
            if cols[i][j] == '#':
                galaxies.append((i, j))
                print(f"Found galaxy: {(j, i)}")                
        
    return galaxies


def calc_distance(gal_1: tuple, gal_2: tuple) -> int:
    return abs(gal_1[0] - gal_2[0]) + abs(gal_1[1] - gal_2[1])            


def run():
    FCHECK = 'input_check'
    FPROD = 'd11/input'
    res = 0
    inp = utils.read_file_lines(FPROD)
    galaxies = get_data_doubled(inp)
    for gal_1 in galaxies:
        for gal_2 in galaxies:
            res += calc_distance(gal_1, gal_2)
    res /= 2            
    print(f"\n====\nResult: {res}")
