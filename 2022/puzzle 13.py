from functools import cmp_to_key

def compare(p1, p2):
    if type(p1) is list and type(p2) is list:
        for i in range(len(p1)):
            if i >= len(p2):
                return 0
            if compare(p1[i], p2[i]):
                return 1
            else:
                return 0
            # elif compare(p2[i], p1[i]):
            #     return 0
        if len(p1) < len(p2):
            return 1
    elif type(p1) is int and type(p2) is int:
        return p1 < p2
    else:
        if type(p1) is int:
            return compare([p1], p2)
        else:
            return compare(p1, [p2])

def compare2(p1, p2):
    if compare(p1, p2):
        return -1
    elif compare(p2, p1):
        return 1
    else:
        return 0
    

with open('input/puzzle 13', 'r') as f:
    pairs = f.read().split('\n\n')
    indecis = []
    ordered = []
    for i, pair in enumerate(pairs):
        lines = pair.split('\n')
        p1 = eval(lines[0])
        p2 = eval(lines[1])
        if compare(p1, p2):
            indecis.append(i+1)
        
        ordered.append(p1)
        ordered.append(p2)

    ordered.append([[2]])
    ordered.append([[6]])
    
    ordered.sort(key=cmp_to_key(compare2))
        
    print(sum(indecis))

    print((ordered.index([[2]])+1)*(ordered.index([[6]])+1))










    
