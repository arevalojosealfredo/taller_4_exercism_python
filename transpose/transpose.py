from itertools import zip_longest


def transpose(lines):
    return "\n".join(
        "".join(block).rstrip("\n").replace("\n", " ") for block
        in zip_longest(*lines.splitlines(), fillvalue="\n")
    )