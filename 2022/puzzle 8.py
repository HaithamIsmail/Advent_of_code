import numpy as np

with open('input/puzzle 8', 'r') as f:
    input_ = f.read().split('\n')
    grid = np.empty([len(input_), len(input_[0])])
    scores = np.zeros([len(input_), len(input_[0])])
    for i, line in enumerate(input_):
        grid[i, :] = [int(e) for e in line]
    
    total_p1 = grid.shape[0]*2 + grid.shape[1]*2 - 4
    
    for i in range(1,grid.shape[0]-1):
        for j in range(1, grid.shape[1]-1):
            top = [grid[i, j] > tree for tree in grid[0:i, j]]
            bot = [grid[i, j] > tree for tree in grid[i+1:grid.shape[0], j]]
            left = [grid[i, j] > tree for tree in grid[i, 0:j]]
            right = [grid[i, j] > tree for tree in grid[i, j+1:grid.shape[1]]]
            if grid[i, j] != 0.:
                total_p1 += (all(top) or all(bot) or all(left) or all(right))
                
                top.reverse()
                left.reverse()
                s_top = top.index(False)+1 if False in top else i
                s_bot = bot.index(False)+1 if False in bot else grid.shape[0]-(i+1)
                s_left = left.index(False)+1 if False in left else j
                s_right = right.index(False)+1 if False in right else grid.shape[1]-(j+1)
                scores[i, j] = s_top*s_bot*s_left*s_right
            else:
                scores[i, j] = 1
            
    print(total_p1)
    print(np.max(scores))