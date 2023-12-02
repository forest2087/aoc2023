import shutil
import utils
import sys
import os
import importlib

from datetime import datetime
from aocd import get_data

# python main.py 1 s 1
# python main.py 1 i 2
# type, part, day
arguments = sys.argv[1:]  # Skip the script name


INPUTTXT = arguments[0] if len(arguments) > 0 else 's'
PART = arguments[1] if len(arguments) > 1 else 1
CURRENT_DAY = str(arguments[2]) if len(
    arguments) > 2 else str(datetime.now().day)


def readFile():
    if INPUTTXT == 's':
        f = open(CURRENT_DAY + '/sample.txt', 'r')
    if INPUTTXT == 'i':
        f = open(CURRENT_DAY + '/input.txt', 'r')
    return f


def solv():
    sys.path.append(CURRENT_DAY)
    mod = importlib.import_module('day'+str(CURRENT_DAY))
    f = readFile()

    func = getattr(mod, 'solv' + str(PART))
    func(f)


def run():
    print('Day - ', CURRENT_DAY)
    print('Input - ', INPUTTXT)
    print('Part - ', PART)
    path = CURRENT_DAY
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
        print('create')
      # Create a new directory because it does not exist
        os.makedirs(path)
        f = open(path + '/sample.txt', 'x')
        f.close()
        f = open(path + '/input.txt', 'x')
        f.write(get_data(day=int(CURRENT_DAY), year=2023))
        f.close()
        shutil.copyfile('example.py', path + '/day'+CURRENT_DAY+'.py')
        print("Day" + CURRENT_DAY + " is created!")
    else:
        solv()

# for i in range(1, CURRENT_DAY+1):
#     print('*'*30)
#     print('Day ', i, ':')
#     for j in range(1, 3):
#         print('\tPart ', j)
#         print('\t\tsample', '-'*2)
#         run(str(i), 's', j)
#         print('\t\tinput', '-'*2)
#         run(str(i), 'i', j)


if __name__ == "__main__":
    run()
    # print(get_data(day=CURRENT_DAY, year=2023))
