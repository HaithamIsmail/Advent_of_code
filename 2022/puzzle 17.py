rocks = [
    [0, 1, 2, 3],
    [1, 1j, 1+1j, 2+1j, 1+2j],
    [0, 1, 2, 2+1j, 2+2j],
    [0, 1j, 2j, 3j],
    [0, 1, 1j, 1+1j]
]
with open('input/puzzle 17', 'r') as f:
    input_ = f.read()
    
jets = [1 if x == '>' else -1 for x in input_]
solid = {x-1j for x in range(7)}
height = 0

counter = 0
rock_index = 0
# position next rock
rock_p = {x+2 + (height+3)*1j for x in rocks[rock_index]}

while counter < 2022:
    for jet in jets:
        moved = {x+jet for x in rock_p}
        if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
            rock_p = moved
        
        moved = {x-1j for x in rock_p}
        
        # print(moved & solid)
        if moved & solid:
            solid |= rock_p
            counter +=1 
            height = max(x.imag for x in solid) + 1 
            if counter >= 2022: break
            rock_index = (rock_index+1)%5
            rock_p = {x + 2 + (height + 3)*1j for x in rocks[rock_index]}
        else:
            rock_p = moved

print(int(height))

P2 = 1000000000000

solid = {x-1j for x in range(7)}
height = 0

counter = 0
rock_index = 0
# position next rock
rock_p = {x+2 + (height+3)*1j for x in rocks[rock_index]}
seen = {}

def normalize():
    ''' find the maximum height at each x then normalizes such that max height = 0 '''
    temp = [-1]*7
    for x in solid:
        r = int(x.real)
        i = int(x.imag)
        temp[r] = max(temp[r], i)
    
    top = max(temp)
    return tuple(x-top for x in temp)
    

while counter < P2:
    for ji, jet in enumerate(jets):
        moved = {x+jet for x in rock_p}
        if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
            rock_p = moved
        
        moved = {x-1j for x in rock_p}
        
        # print(moved & solid)
        if moved & solid:
            solid |= rock_p
            counter +=1 
            height = max(x.imag for x in solid) + 1 
            if counter >= P2: break
            rock_index = (rock_index+1)%5
            rock_p = {x + 2 + (height + 3)*1j for x in rocks[rock_index]}
            key = (ji, rock_index, normalize())
            if key in seen:
                last_counter, last_height = seen[key]
                remaining = P2 - counter
                repeat = remaining // (counter - last_counter)
                offset = repeat * (height - last_height)
                counter += repeat * (counter - last_counter)
                seen = {}
            seen[key] = (counter, height)
        else:
            rock_p = moved
            
print(int(height+ offset))
