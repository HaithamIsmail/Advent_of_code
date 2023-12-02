word_to_digit = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

with open('input.txt', 'r') as f:

    nums = []
    for line in f:
        first = None
        last = None
        for i, ch in enumerate(line):
            if ch.isdigit():
                if first is None:
                    first = int(ch)
                last = int(ch)
            else:
                for digit in word_to_digit:
                    if i + len(digit) <= len(line):
                        word_digit = line[i : i+len(digit)]
                        if word_digit in word_to_digit:
                            if first is None:
                                first = word_to_digit[word_digit]
                            last = word_to_digit[word_digit]
        nums.append(first*10 + last)

    print(sum(nums))