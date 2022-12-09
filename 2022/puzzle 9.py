import re
import math

class knot:
    def __init__(self, parent= None) -> None:
        self.coord = [0, 0]
        self.parent:knot = parent
    
    def follow(self):
        if self.parent != None: 
            if abs(self.coord[0] - self.parent.coord[0]) > 1 or abs(self.coord[1] - self.parent.coord[1]) > 1:
                self.coord[0] += (1 if self.parent.coord[0]>self.coord[0] else -1 if self.parent.coord[0]<self.coord[0] else 0)
                self.coord[1] += (1 if self.parent.coord[1]>self.coord[1] else -1 if self.parent.coord[1]<self.coord[1] else 0)
        

with open('input/puzzle 9', 'r') as f:
    data = re.findall("(\S) (\d+)", f.read())
    data = [[e[0], int(e[1])] for e in data]
    h = knot(None)
    knots = []
    knots.append(knot(h))
    for i in range(1, 9):
        knots.append(knot(knots[i-1]))
    
    s_p1 = set()
    s_p1.add(tuple(knots[0].coord))
    
    s_p2 = set()
    s_p2.add(tuple(knots[8].coord))
    
    for move, amt in data:
        for i in range(amt):
            if move == 'U':
                h.coord[1] += 1
            elif move == 'D':
                h.coord[1] -= 1
            elif move == 'R':
                h.coord[0] += 1
            elif move == 'L':
                h.coord[0] -= 1
                
            for i in knots:
                i.follow()

            s_p1.add(tuple(knots[0].coord))
            s_p2.add(tuple(knots[8].coord))
    
    print(len(s_p1))
    print(len(s_p2))