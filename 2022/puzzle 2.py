def check_result_part1(choices):
    total = 0
    if choices[1] == 'X':
        total += 1
        if choices[0] == 'A':
            total += 3
        elif choices[0] == 'C':
            total += 6
    elif choices[1] == 'Y':
        total += 2
        if choices[0] == 'B':
            total += 3
        elif choices[0] == 'A':
            total += 6
    elif choices[1] == 'Z':
        total += 3
        if choices[0] == 'C':
            total += 3
        elif choices[0] == 'B':
            total += 6
    return total

def check_result_part2(choices):
    total = 0
    hand = ''
    if choices[1] == 'X':
        if choices[0] == 'A':
            hand = 'C'
        elif choices[0] == 'B':
            hand = 'A'
        else:
            hand = 'B'
            
    elif choices[1] == 'Y':
        total += 3
        if choices[0] == 'A':
            hand = 'A'
        elif choices[0] == 'B':
            hand = 'B'
        else:
            hand = 'C'
            
    elif choices[1] == 'Z':
        total += 6
        if choices[0] == 'A':
            hand = 'B'
        elif choices[0] == 'B':
            hand = 'C'
        else:
            hand = 'A'
    
    if hand == 'A':
        total += 1
    elif hand == 'B':
        total += 2
    else:
        total += 3
        
    return total

with open('input/puzzle 2', 'r') as f:
    input_ = f.read().split('\n')
    score1 = 0
    score2 = 0
    for line in input_:
        line = line.split(' ')
        score1 += check_result_part1(line)
        score2 += check_result_part2(line)

print('part 1:', score1)
print('part 2:', score2)