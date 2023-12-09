import utils
from collections import Counter


def get_instructions(row: str) -> list:
    res = []
    return [i for i in row]


def get_nodes(input: list) -> dict:
    res = {}
    for row in input:
        node = row.split(" = ")[0]
        left = row.split(" = ")[1][1:4]
        right = row.split(" = ")[1][6:9]
        res[node] = (left, right)
    return res


def use_instruction(input_node: str, instruction: str, nodes: dict) -> str:
    if instruction == 'L':
        return nodes[input_node][0]
    return nodes[input_node][1]


def use_instruction_multi(input_nodes: list, instruction: str, nodes: dict) -> list:
    res = []
    if instruction == 'L':
        for i in input_nodes:
            res.append(nodes[i][0])
        return res
    
    for i in input_nodes:
        res.append(nodes[i][1])
    return res

    
def use_instructions(instr: list, nodes: dict, last_node: str = 'AAA', last_steps: int = 0) -> tuple:
    res_node = last_node
    for i in instr:
        last_steps += 1
        if res_node[2] == 'Z':
            return last_steps
    print(f"Didn't find exit, last_node: {res_node}, last_steps:{last_steps}")
    return use_instructions(instr, nodes, res_node, last_steps)
      

def test():
    t = "32748 765"
    print(t)


def run():
    FCHECK = 'input_check'
    FPROD = 'd8/input'
    inp = utils.read_file_lines(FPROD)
    res = 0
    nodes = []
    instr = get_instructions(inp[0])
    nodes = get_nodes(inp[2:])
    res = use_instructions(instr, nodes)
    print(f"\n====\nResult: {res}")
