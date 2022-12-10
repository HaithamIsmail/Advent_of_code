cycle = 0
v = 1
values = []

def tick_cycle():
    global cycle, v, values
    if cycle % 40 in range(v-1, v+2):
        print("#", end="")
    else:
        print(".", end="")
    cycle += 1
    if cycle % 40 == 0:
        print("")
    if cycle in [20, 60, 100, 140, 180, 220]:
        values.append(cycle*v)


with open('input/puzzle 10', 'r') as f:
    lines = f.read().split('\n')
    for line in lines:
        if line == 'noop':
            tick_cycle()
        else:
            tick_cycle()
            tick_cycle()
            v += int(line[5:])
            
    print('part 1: ', sum(values))
            