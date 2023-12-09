import utils
import sys
from collections import Counter


def get_instructions(row: str) -> list:
    return [i for i in row]


def get_nodes(input: list) -> dict:
    res = {}
    for row in input:
        node = row.split(" = ")[0]
        left = row.split(" = ")[1][1:4]
        right = row.split(" = ")[1][6:9]
        res[node] = (left, right)
    return res


def use_instruction_multi(input_nodes: list, instruction: str, nodes: dict) -> list:
    res = []
    if instruction == 'L':
        for i in input_nodes:
            res.append(nodes[i][0])
        # print(f"Go left from {input_nodes} to {res}")
        return res
    
    for i in input_nodes:
        res.append(nodes[i][1])
    # print(f"Go right from {input_nodes} to {res}")
    return res


def use_instructions_multi(instr: list, nodes: dict, last_nodes: list, last_steps: int = 0) -> tuple:
    res_nodes = last_nodes
    for i in instr:
        res_nodes = use_instruction_multi(res_nodes, i, nodes)
        last_steps += 1
        if all(r[2] == 'Z' for r in res_nodes):
            return last_steps
    # print(f"Didn't find exit, last_node: {res_nodes}, last_steps:{last_steps}")
    return use_instructions_multi(instr, nodes, res_nodes, last_steps)
    

def test():
    t = "32748 765"
    print(t)


def run():
    sys.setrecursionlimit(100000000)
    FCHECK = 'input_check'
    FPROD = 'd8/input'
    inp = utils.read_file_lines(FPROD)
    res = 0
    nodes = []
    instr = get_instructions(inp[0])
    nodes = get_nodes(inp[2:])
    start_nodes = []
    for k, v in nodes.items():
        if k[2] == 'A':
            start_nodes.append(k)
    res = use_instructions_multi(instr, nodes, start_nodes)
    print(f"\n====\nResult: {res}")

