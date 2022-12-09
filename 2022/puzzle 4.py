with open('input/puzzle 4', 'r') as f:
    input_ = f.read().split('\n')
    total_p1 = 0
    total_p2 = 0
    for line in input_:
        l = [[int(e) for e in item.split('-')] for item in line.split(',')]
        
        if (l[0][0] <= l[1][0] <= l[1][1] <= l[0][1]) or (l[1][0] <= l[0][0] <= l[0][1] <= l[1][1]):
            total_p1 += 1
        if max(l[0][0], l[1][0]) <= min(l[0][1], l[1][1]):
            total_p2 += 1
            
    print('part 1:', total_p1)
    print('part 2:', total_p2)