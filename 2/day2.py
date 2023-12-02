import re
from aocd import submit
import math


def readInput(f):
    while True:
        ln = f.readline()

        if not ln:
            break


def solv1(f):
    game = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    ret = 0

    while True:
        ln = f.readline()

        if not ln:
            break

        g = re.search(r'Game (\d+):', ln).group(1)

        # print(g)

        bags = re.split(r";\s*", ln.split(":", 1)[1])

        valid = True
        for bag in bags:
            balls = re.findall(r'(\d+) (\w+)', bag)
            for n, c in balls:
                # print(int(n), c)
                if int(n) > game.get(c):
                    valid = False
                    break

        if valid:
            ret += int(g)

    return ret


def solv2(f):

    ret = 0

    while True:
        ln = f.readline()

        if not ln:
            break

        g = re.search(r'Game (\d+):', ln).group(1)

        # print(g)

        bags = re.split(r";\s*", ln.split(":", 1)[1])

        valid = True

        lowest = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for bag in bags:
            balls = re.findall(r'(\d+) (\w+)', bag)
            for n, c in balls:
                if int(n) > lowest.get(c):
                    lowest[c] = int(n)
        ret += math.prod(lowest.values())
    return ret
