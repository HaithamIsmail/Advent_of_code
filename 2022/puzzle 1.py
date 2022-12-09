
sum_ = 0
sum_list = []

with open('input/puzzle 1', 'r') as f:
    input_ = f.read().split('\n')
    for line in input_:
        if line == '':
            sum_list.append(sum_)
            sum_ = 0
        else:
            sum_ += int(line)

sum_list = sorted(sum_list)

print('part 1:', sum_list[-1])
print('part 2:', sum(sum_list[-3:]))

    