import re
from itertools import zip_longest
from copy import deepcopy

def p1(data, stack1):
    for n, from_, to in data:
        for i in range(int(n)):
            stack1[int(to)-1].append(stack1[int(from_)-1].pop())
    for s in stack1:
        print(s[-1], end="")

def p2(data, stack2):
    for n, from_, to in data:
        stack2[int(to)-1] = stack2[int(to)-1] + stack2[int(from_)-1][-int(n):]
        stack2[int(from_)-1] = stack2[int(from_)-1][:-int(n)]
    for s in stack2:
        print(s[-1], end="")

with open('input/puzzle 5', 'r') as f:
    crates, moves = f.read().split("\n\n")
    crates = crates.splitlines()[:-1]
    crates = [crate[1::4] for crate in crates]
    crates = [*zip_longest(*crates[::-1], fillvalue=" ")]
    crates = [[e for e in crate if not e.isspace()] for crate in crates]
    
    print(crates)
    
    moves = re.findall(r"move (\d+) from (\d) to (\d)", moves)
    p1(moves, deepcopy(crates))
    print('')
    p2(moves, deepcopy(crates))