import utils
from dataclasses import dataclass


@dataclass
class Neighbours:
    top: list[str]
    right: list[str]
    bot: list[str]
    left: list[str]

MAZE_WIDTH = 140
MAZE_HEIGHT = 140


def get_maze(inp: list) -> list:
    res = []
    for i, line in enumerate(inp):
        res.append(line)
    return res


def find_animal(maze: list) -> tuple:
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                return (i, j)
    return(-1, -1)


def is_tiles_at_coord(tiles: list, coord: tuple, maze: list) -> bool:
    if coord[0] < 0 or coord[0] >= MAZE_HEIGHT:
        return False
    if coord[1] < 0 or coord[1] >= MAZE_WIDTH:
        return False
    if maze[coord[0]][coord[1]] in tiles:
        return True
    return False


def find_next_pipe_coord(maze: list, coord_from: tuple, coord_remove: tuple = None) -> tuple:
    rules = {
        'S': Neighbours(['|', '7', 'F'], ['-', 'J', '7'], ['|', 'L', 'J'], ['-', 'L', 'F']),
        '|': Neighbours(['|', '7', 'F', 'S'], [], ['|', 'L', 'J', 'S'], []),
        '-': Neighbours([], ['-', 'J', '7', 'S'], [], ['-', 'L', 'F', 'S']),
        'L': Neighbours(['|', '7', 'F', 'S'], ['-', 'J', '7', 'S'], [], []),
        'J': Neighbours(['|', '7', 'F', 'S'], [], [], ['-', 'L', 'F', 'S']),
        '7': Neighbours([], [], ['|', 'L', 'J', 'S'], ['-', 'L', 'F', 'S']),
        'F': Neighbours([], ['-', 'J', '7', 'S'], ['|', 'L', 'J', 'S'], [])
    }
    next_pipe_coords = []
    this_pipe = maze[coord_from[0]][coord_from[1]]
    
    test_coords = (coord_from[0] - 1, coord_from[1])
    if is_tiles_at_coord(rules[this_pipe].top, test_coords, maze):
        next_pipe_coords.append(test_coords)
    
    test_coords = (coord_from[0], coord_from[1] + 1)
    if is_tiles_at_coord(rules[this_pipe].right, test_coords, maze):
        next_pipe_coords.append(test_coords)
        
    test_coords = (coord_from[0] + 1, coord_from[1])
    if is_tiles_at_coord(rules[this_pipe].bot, test_coords, maze):
        next_pipe_coords.append(test_coords)
        
    test_coords = (coord_from[0], coord_from[1] - 1)
    if is_tiles_at_coord(rules[this_pipe].left, test_coords, maze):
        next_pipe_coords.append(test_coords)   
        
    if coord_remove:
        next_pipe_coords.remove(coord_remove)            
        
    return next_pipe_coords[0]


def calc_maze(maze: list) -> int:
    coord_prev = find_animal(maze)
    path = [coord_prev]
    print(f"Start coord: {coord_prev}")
    next_coord = find_next_pipe_coord(maze, coord_prev)
    path.append(next_coord)
    print(f"Found next pipe at coord: {next_coord}")

    while maze[next_coord[0]][next_coord[1]] != 'S':
        next_coord = find_next_pipe_coord(maze, next_coord, path[-2])
        path.append(next_coord)
        print(f"Found next pipe at coord: {next_coord}")
    return (len(path) - 1) / 2


def test():
    t = "32748 765"
    print(t)


def run():
    FCHECK = 'input_check'
    FPROD = 'd10/input'
    inp = utils.read_file_lines(FPROD)
    res = 0
    maze = get_maze(inp)
    res = calc_maze(maze)
    print(f"\n====\nResult: {res}")
