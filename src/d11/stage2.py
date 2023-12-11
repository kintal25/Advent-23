import utils


def get_galaxies(inp: list[str]) -> list[tuple]:
    galaxies = []    
    for i, line in enumerate(inp):
        for j in range(len(inp[0])):
            if inp[i][j] == '#':
                galaxies.append((i, j))
                print(f"Found galaxy: {(i, j)}")           
    return galaxies


def get_row_expansions(inp: list[str]) -> list[int]:
    row_expansions = []
    for i, line in enumerate(inp):
        if all(x == '.' for x in line):
            print(f"Row expansion {i}")
            row_expansions.append(i)  
    return row_expansions      


def get_col_expansions(inp: list[str]) -> list[int]:        
    col_expansions = []
    for j in range(len(inp[0])):
        col = ''
        for i in range(len(inp)):
            col += inp[i][j]        
        if all(x == '.' for x in col):
            print(f"Column expansion {j}")
            col_expansions.append(j)    
    return col_expansions            


def calc_distance(gal_1: tuple, gal_2: tuple, row_expansions: list[int], col_expansions: list[int]) -> int:
    EXPANSION = 1000000
    
    row_distance = abs(gal_1[0] - gal_2[0])
    for row_exp in row_expansions:
        if (row_exp > gal_1[0] and row_exp < gal_2[0]) or (row_exp > gal_2[0] and row_exp < gal_1[0]):
            row_distance += (EXPANSION - 1)

    col_distance = abs(gal_1[1] - gal_2[1])
    for col_exp in col_expansions:
        if (col_exp > gal_1[1] and col_exp < gal_2[1]) or (col_exp > gal_2[1] and col_exp < gal_1[1]):
            col_distance += (EXPANSION - 1)            
         
    return row_distance + col_distance       


def run():
    FCHECK = 'input_check'
    FPROD = 'd11/input'
    res = 0
    inp = utils.read_file_lines(FPROD)
    galaxies = get_galaxies(inp)
    row_expansions = get_row_expansions(inp)
    col_expansions = get_col_expansions(inp)
    for gal_1 in galaxies:
        for gal_2 in galaxies:
            res += calc_distance(gal_1, gal_2, row_expansions, col_expansions)
            # print(f"Distance between gals {gal_1} and {gal_2} is {calc_distance(gal_1, gal_2, row_expansions, col_expansions)}")
    res /= 2            
    print(f"\n====\nResult: {res}")
