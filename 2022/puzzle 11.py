import math
import operator

ops = { "+": operator.add, "-": operator.sub, "*": operator.mul }

def p1(data):
    items = []
    operation = []
    test = []
    test = []
    true_ = []
    false_ = []
    for m in data:
        lines = m.split("\n")
        for line in lines:
            line = line.strip().split(' ')
            if line[0] == 'Starting':
                items.append([int(num.split(',')[0]) for num in line[2:]])
            elif line[0] =='Operation:':
                operation.append([line[4], line[5]])
            elif line[0] == 'Test:':
                test.append(int(line[3]))
            elif line[1] == 'true:':
                true_.append(int(line[5]))
            elif line[1] == 'false:':
                false_.append(int(line[5]))
                
    inspects = [0]*len(items)
    for i in range(20):
        for j in range(len(items)):
            while len(items[j]) > 0:
                inspects[j] += 1
                item = items[j].pop(0)
                if operation[j][1] != 'old':
                    new = ops[operation[j][0]](item, int(operation[j][1]))//3
                else:
                    new = ops[operation[j][0]](item, item)//3
                   
                if new % test[j] == 0:
                    items[true_[j]].append(new)
                else:
                    items[false_[j]].append(new)
          
    inspects = sorted(inspects)          
    return inspects[-1]*inspects[-2]

def p2(data):
    items = []
    operation = []
    test = []
    test = []
    true_ = []
    false_ = []
    for m in data:
        lines = m.split("\n")
        for line in lines:
            line = line.strip().split(' ')
            if line[0] == 'Starting':
                items.append([int(num.split(',')[0]) for num in line[2:]])
            elif line[0] =='Operation:':
                operation.append([line[4], line[5]])
            elif line[0] == 'Test:':
                test.append(int(line[3]))
            elif line[1] == 'true:':
                true_.append(int(line[5]))
            elif line[1] == 'false:':
                false_.append(int(line[5]))
                
    inspects = [0]*len(items)
    mod = math.prod(test)
    for i in range(10000):
        for j in range(len(items)):
            while len(items[j]) > 0:
                inspects[j] += 1
                item = items[j].pop(0)
                if operation[j][1] != 'old':
                    new = ops[operation[j][0]](item, int(operation[j][1])) % mod
                else:
                    new = ops[operation[j][0]](item, item) % mod
                   
                if new % test[j] == 0:
                    items[true_[j]].append(new)
                else:
                    items[false_[j]].append(new)
          
    inspects = sorted(inspects)          
    return inspects[-1]*inspects[-2]

with open('input/puzzle 11', 'r') as f:
    data = f.read().split("\n\n")

    print(p1(data))
    print(p2(data))
                
    