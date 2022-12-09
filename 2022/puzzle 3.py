def part1(line):
    length = len(line)
    if length % 2 == 0:
        comp1 = line[:int(length/2)]
        comp2 = line[int(length/2):]
    else:
        comp1 = line[:int(length/2)+1]
        comp2 = line[int(length/2)+1:]
    
    for item in comp1:
        if item in comp2:
            if item >= 'a' and item <= 'z':
                total = ((ord(item)%ord('a'))+1)
            else:
                total = ((ord(item)%ord('A'))+27)
            break
    return total

def part2(lines):
    for item in lines[0]:
        if item in lines[1] and item in lines[2]:
            if item >= 'a' and item <= 'z':
                total = ((ord(item)%ord('a'))+1)
            else:
                total = ((ord(item)%ord('A'))+27)
            break
    return total
            
with open('input/puzzle 3', 'r') as f:
    input_ = f.read().split('\n')
    total_p1 = 0
    for line in input_:
        total_p1 += part1(line)
        
    i=0
    total_p2 = 0
    while i < len(input_):
        total_p2 += part2(input_[i:i+3])
        i += 3
    
        
print('part 1:', total_p1)
print('part 2:', total_p2)