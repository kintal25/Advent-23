def read_file(filename: str, with_newlines = False):
    with open(filename, 'r') as f:
        res = f.read()
    if not with_newlines:
        return res.replace("\n", "")
    return res


def read_file_lines(filename: str):
    with open(filename, 'r') as f:
        return f.read().splitlines()