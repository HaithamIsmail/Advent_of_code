import re

def cannot(coordinates, y):
    beacons = set()     
    intervals = []
    for x1, y1, x2, y2 in coordinates:
        dist = abs(x1-x2) + abs(y1-y2)
        diff = dist - abs(y1-y)
        
        if diff < 0:
            continue
        
        # get Xs where the distance is equal to distance to beacon
        lowX = x1 - diff
        highX = x1 + diff
        
        intervals.append([lowX, highX])
        
        if y2 == y:
            beacons.add(x2)
            
    intervals.sort()
    y20k_interval = []
    for interval in intervals:
        if not y20k_interval:
            y20k_interval.append(interval)
            continue
        
        lowX, highX = y20k_interval[-1]
        if interval[0] > highX + 1:
            y20k_interval.append(interval)
            continue
        
        y20k_interval[-1][1] = max(highX, interval[1])
        # y20k_interval[-1][0] = min(lowX, interval[0])
    
    return beacons, y20k_interval

with open('input/puzzle 15', 'r') as f:
    coordinates = re.findall('Sensor at x=(\d+), y=(\d+): closest beacon is at x=(\d+), y=(\d+)', f.read())
    coordinates = [[int(x1), int(y1), int(x2), int(y2)] for x1,y1,x2,y2 in coordinates]

Y = 2000000
beacons, y20k_interval = cannot(coordinates, Y)
y20k = set()
for lowX, highX in y20k_interval:
    for x in range(lowX, highX+1):
        y20k.add(x)
print(len(y20k-beacons))

M = 4000000
for y in range(M+1):
    _, intervals = cannot(coordinates, y)
    
    x=0
    for lowX, highX in intervals:
        if x < lowX:
            print(x*M+y)
            break
        x = max(x, highX+1)
        if x > M:
            break
    
    