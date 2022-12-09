with open('input/puzzle 6', 'r') as f:
    s = f.read().strip()
    for i in range(len(s)-3):
        if len(set(s[i:i+4])) == 4:
            print(i+4)
            break
    for i in range(len(s)-13):
        if len(set(s[i:i+14])) == 14:
            print(i+14)
            break
    