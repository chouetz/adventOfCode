import argparse
import re
from collections import namedtuple

parser = argparse.ArgumentParser()
parser.add_argument("part", help="game part", type=int)
parser.add_argument("-t", "--test", action="store_true")
args = parser.parse_args()
test = f"-{args.part}-test" if args.test else ""
file_name = f"{__file__.split('/')[-1].split('.')[0]}{test}.txt"


Point = namedtuple("Point", ["x", "y"])
numbers = ['1','2','3','4','5','6','7','8','9','0','.']
if args.part == 1:
    # Part 1
    with open(file_name, "r") as f:
        lines = f.readlines()
    width, height = len(lines[0])-1, len(lines)
    symbols = []
    matrix = []
    for row, line in enumerate(lines):
        matrix.append(list(line.strip()))
        for col, c in enumerate(matrix[-1]):
            if c not in numbers:
                symbols.append(Point(col, row))
    total = 0
    # print(matrix)
    for symbol in symbols:
        print(symbol)
        # complète à gauche`
        if symbol.x - 1 >= 0 and matrix[symbol.y][symbol.x-1].isdigit():
            idx = symbol.x - 1
            num = matrix[symbol.y][idx]
            while idx - 1 >= 0 and matrix[symbol.y][idx - 1].isdigit():
                idx -= 1
                num = matrix[symbol.y][idx] + num
            # print(symbol, num)
            total += int(num)
        # complète à droite
        if symbol.x + 1 < width and matrix[symbol.y][symbol.x + 1].isdigit():
            idx = symbol.x + 1
            num = matrix[symbol.y][idx]
            while idx + 1 < width and matrix[symbol.y][idx + 1].isdigit():
                idx += 1
                num += matrix[symbol.y][idx]
            # print(symbol, num)
            total += int(num)
        # complète en haut
        if symbol.y - 1 >= 0 and matrix[symbol.y - 1][symbol.x].isdigit():
            idx = symbol.x
            num = matrix[symbol.y - 1][symbol.x]
            while idx - 1 >= 0 and matrix[symbol.y - 1][idx - 1].isdigit():
                idx -= 1
                num = matrix[symbol.y - 1][idx] + num
            idx = symbol.x
            while idx + 1 < width and matrix[symbol.y- 1][idx+1].isdigit():
                idx += 1
                num += matrix[symbol.y - 1][idx]
            # print(symbol, num)
            total += int(num)
        else:
            # complète en haut à gauche
            if symbol.y - 1 >= 0 and symbol.x - 1 >= 0 and matrix[symbol.y - 1][symbol.x - 1].isdigit():
                idx = symbol.x - 1
                num = matrix[symbol.y-1][idx]
                while idx - 1 >= 0 and matrix[symbol.y-1][idx - 1].isdigit():
                    idx -= 1
                    num = matrix[symbol.y-1][idx] + num
                # print(symbol, num)
                total += int(num)
            # complète en haut à droite
            if symbol.y - 1 >= 0 and symbol.x + 1 < width and matrix[symbol.y - 1][symbol.x + 1].isdigit():
                idx = symbol.x + 1
                num = matrix[symbol.y-1][idx]
                while idx + 1 < width and matrix[symbol.y-1][idx + 1].isdigit():
                    idx += 1
                    num += matrix[symbol.y-1][idx]
                # print(symbol, num)
                total += int(num)
        # complète en bas
        if symbol.y + 1 < height and matrix[symbol.y + 1][symbol.x].isdigit():
            idx = symbol.x
            num = matrix[symbol.y + 1][symbol.x]
            while idx - 1 >= 0 and matrix[symbol.y + 1][idx - 1].isdigit():
                idx -= 1
                num = matrix[symbol.y + 1][idx] + num
            idx = symbol.x
            while idx + 1 < width and matrix[symbol.y+ 1][idx+1].isdigit():
                idx += 1
                num += matrix[symbol.y + 1][idx]
            # print(symbol, num)
            total += int(num)
        else:
            # complète en bas à gauche
            if symbol.y + 1 < height and symbol.x - 1 >= 0 and matrix[symbol.y + 1][symbol.x - 1].isdigit():
                idx = symbol.x - 1
                num = matrix[symbol.y+1][idx]
                while idx - 1 >= 0 and matrix[symbol.y+1][idx - 1].isdigit():
                    idx -= 1
                    num = matrix[symbol.y+1][idx] + num
                # print(symbol, num)
                total += int(num)
            # complète en bas à droite
            if symbol.y + 1 < height and symbol.x + 1 < width and matrix[symbol.y + 1][symbol.x + 1].isdigit():
                idx = symbol.x + 1
                num = matrix[symbol.y+1][idx]
                while idx + 1 < width and matrix[symbol.y+1][idx + 1].isdigit():
                    idx += 1
                    num += matrix[symbol.y+1][idx]
                # print(symbol, num)
                total += int(num)
    print(total)

if args.part == 2:
      # Part 1
    with open(file_name, "r") as f:
        lines = f.readlines()
    width, height = len(lines[0])-1, len(lines)
    symbols = []
    matrix = []
    for row, line in enumerate(lines):
        matrix.append(list(line.strip()))
        for col, c in enumerate(matrix[-1]):
            if c == '*':
                symbols.append(Point(col, row))
    total = 0
    # print(matrix)
    for symbol in symbols:
        print(symbol)
        part = []
        # complète à gauche`
        if symbol.x - 1 >= 0 and matrix[symbol.y][symbol.x-1].isdigit():
            idx = symbol.x - 1
            num = matrix[symbol.y][idx]
            while idx - 1 >= 0 and matrix[symbol.y][idx - 1].isdigit():
                idx -= 1
                num = matrix[symbol.y][idx] + num
            # print(symbol, num)
            part.append(int(num))
        # complète à droite
        if symbol.x + 1 < width and matrix[symbol.y][symbol.x + 1].isdigit():
            idx = symbol.x + 1
            num = matrix[symbol.y][idx]
            while idx + 1 < width and matrix[symbol.y][idx + 1].isdigit():
                idx += 1
                num += matrix[symbol.y][idx]
            # print(symbol, num)
            part.append(int(num))
        # complète en haut
        if symbol.y - 1 >= 0 and matrix[symbol.y - 1][symbol.x].isdigit():
            idx = symbol.x
            num = matrix[symbol.y - 1][symbol.x]
            while idx - 1 >= 0 and matrix[symbol.y - 1][idx - 1].isdigit():
                idx -= 1
                num = matrix[symbol.y - 1][idx] + num
            idx = symbol.x
            while idx + 1 < width and matrix[symbol.y- 1][idx+1].isdigit():
                idx += 1
                num += matrix[symbol.y - 1][idx]
            # print(symbol, num)
            part.append(int(num))
        else:
            # complète en haut à gauche
            if symbol.y - 1 >= 0 and symbol.x - 1 >= 0 and matrix[symbol.y - 1][symbol.x - 1].isdigit():
                idx = symbol.x - 1
                num = matrix[symbol.y-1][idx]
                while idx - 1 >= 0 and matrix[symbol.y-1][idx - 1].isdigit():
                    idx -= 1
                    num = matrix[symbol.y-1][idx] + num
                # print(symbol, num)
                part.append(int(num))
            # complète en haut à droite
            if symbol.y - 1 >= 0 and symbol.x + 1 < width and matrix[symbol.y - 1][symbol.x + 1].isdigit():
                idx = symbol.x + 1
                num = matrix[symbol.y-1][idx]
                while idx + 1 < width and matrix[symbol.y-1][idx + 1].isdigit():
                    idx += 1
                    num += matrix[symbol.y-1][idx]
                # print(symbol, num)
                part.append(int(num))
        # complète en bas
        if symbol.y + 1 < height and matrix[symbol.y + 1][symbol.x].isdigit():
            idx = symbol.x
            num = matrix[symbol.y + 1][symbol.x]
            while idx - 1 >= 0 and matrix[symbol.y + 1][idx - 1].isdigit():
                idx -= 1
                num = matrix[symbol.y + 1][idx] + num
            idx = symbol.x
            while idx + 1 < width and matrix[symbol.y+ 1][idx+1].isdigit():
                idx += 1
                num += matrix[symbol.y + 1][idx]
            # print(symbol, num)
            part.append(int(num))
        else:
            # complète en bas à gauche
            if symbol.y + 1 < height and symbol.x - 1 >= 0 and matrix[symbol.y + 1][symbol.x - 1].isdigit():
                idx = symbol.x - 1
                num = matrix[symbol.y+1][idx]
                while idx - 1 >= 0 and matrix[symbol.y+1][idx - 1].isdigit():
                    idx -= 1
                    num = matrix[symbol.y+1][idx] + num
                # print(symbol, num)
                part.append(int(num))
            # complète en bas à droite
            if symbol.y + 1 < height and symbol.x + 1 < width and matrix[symbol.y + 1][symbol.x + 1].isdigit():
                idx = symbol.x + 1
                num = matrix[symbol.y+1][idx]
                while idx + 1 < width and matrix[symbol.y+1][idx + 1].isdigit():
                    idx += 1
                    num += matrix[symbol.y+1][idx]
                # print(symbol, num)
                part.append(int(num))
        if len(part) == 2:
            total += part[0] * part[1]
    print(total)
    