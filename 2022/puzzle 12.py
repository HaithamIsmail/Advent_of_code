from collections import deque
with open('input/12') as f:
    s=[list(i) for i in f.read().split("\n")]
rows = len(s)
cols = len(s[0])
heights = [[0 for col in range(cols)] for row in range(rows)]

for row in range(rows):
    for column in range(cols):
        if s[row][column]=='S':
            heights[row][column] = 0
            start = (row,column)
        elif s[row][column] == 'E':
            heights[row][column] = 26
            target = (row,column)
        else:
            heights[row][column] = ord(s[row][column])-ord('a')

queue = deque([start])
visited = set()

prev = {}
path = []
while queue:
    row,col = queue.pop()
    if (row,col) in visited:
        continue
    
    for r,c in [(row,col-1), (row,col+1), (row+1,col),(row-1,col)]:
        if r < 0 or c < 0 or r >= rows or c >= cols:
            continue
        if (r,c) in visited:
            continue
        if heights[r][c] - heights[row][col] > 1:
            continue
        if (r,c) == target:
            path = [(r,c)]
            break
        visited.add((row,col))    
        queue.appendleft((r,c))
        prev[(r,c)] = (row, col)

while (row, col) != start:
                row, col = prev[(row, col)]
                path.append((row, col))

print(len(path)-1)