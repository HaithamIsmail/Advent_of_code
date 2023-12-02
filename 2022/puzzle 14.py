import re
from copy import deepcopy

def abyss(sand, rocks):
    abyss = False
    for rock in rocks:
        if rock[0] == sand[0] and sand[1] < rock[1]:
            return True
    return abyss

def find_ground(rocks):
    ground = 0
    for rock in rocks:
        if rock[1] > ground:
            ground = rock[1]
    return ground + 2

with open('input/puzzle 14', 'r') as f:
    data = f.read().split('\n')
    paths = [re.findall('(\d+),(\d+)', path)for path in data]
    rocks = set()
    for path in paths:
        path = [tuple([int(e) for e in coord]) for coord in path]
        for i in range(len(path)-1):
            if path[i][0] != path[i+1][0]:
                for tile in (range(path[i][0], path[i+1][0]+1, 1) if path[i][0] < path[i+1][0] else range(path[i+1][0], path[i][0]+1, 1)):
                    rocks.add((tile, path[i][1]))
            else:
                for tile in (range(path[i][1], path[i+1][1]+1, 1) if path[i][1] < path[i+1][1] else range(path[i+1][1], path[i][1]+1, 1)):
                    rocks.add((path[i][0], tile))
    
    units_1 = 0
    sand = [500, 0]
    rocks_p1 = deepcopy(rocks)
    while abyss(sand, rocks_p1):
        if (sand[0], sand[1]+1) not in rocks_p1:
            sand[1] = sand[1]+1
        elif (sand[0]-1, sand[1]+1) not in rocks_p1:
            sand[0] = sand[0]-1
            sand[1] = sand[1]+1
        elif (sand[0]+1, sand[1]+1) not in rocks_p1:
            sand[0] = sand[0]+1
            sand[1] = sand[1]+1
        else:
            rocks_p1.add(tuple(sand))
            units_1 += 1
            sand = [500, 0]
    print(units_1)

    units_2 = 0
    sand = [500, 0]
    rocks_p2 = deepcopy(rocks)
    ground = find_ground(rocks_p2)
    print(ground)
    while (500, 0) not in rocks_p2:
        if sand[1] == ground-1:
            rocks_p2.add(tuple(sand))
            units_2 += 1
            sand = [500, 0]
        elif (sand[0], sand[1]+1) not in rocks_p2:
            sand[1] = sand[1]+1
        elif (sand[0]-1, sand[1]+1) not in rocks_p2:
            sand[0] = sand[0]-1
            sand[1] = sand[1]+1
        elif (sand[0]+1, sand[1]+1) not in rocks_p2:
            sand[0] = sand[0]+1
            sand[1] = sand[1]+1
        else:
            rocks_p2.add(tuple(sand))
            units_2 += 1
            sand = [500, 0]

    print(units_2)
        

   