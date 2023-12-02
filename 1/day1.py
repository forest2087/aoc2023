import re


def find_first_last_digits(s):
    first, last = None, None
    for c in s:
        if c.isdigit():
            if not first:
                first = c
            last = c
    return first, last


def find_first_last_digits2(s):
    digits = re.findall(
        r'(one|two|three|four|five|six|seven|eight|nine|\d)', s)

    num_dict = {"one": "1", "two": "2", "three": "3", "four": "4",
                "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    digits = [num_dict.get(n, n) for n in digits]
    return digits[0], digits[-1], digits


def solv1(f):
    sum = 0
    while True:
        ln = f.readline()
        if not ln:
            break
        matches = re.findall(r'\d', ln)
        sum += int(matches[0]+matches[-1])
    print(sum)


def solv2(f):
    sum = 0
    while True:
        ln = f.readline()
        if not ln:
            break
        m = re.findall(
            r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', ln)
        d = {"one": "1", "two": "2", "three": "3", "four": "4",
             "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
        m = [d.get(n, n) for n in m]
        sum += int(m[0]+m[-1])
    print(sum)
