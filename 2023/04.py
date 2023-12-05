import argparse

parser = argparse.ArgumentParser()
parser.add_argument("part", help="game part", type=int)
parser.add_argument("-t", "--test", action="store_true")
args = parser.parse_args()
test = f"-{args.part}-test" if args.test else ""
file_name = f"{__file__.split('/')[-1].split('.')[0]}{test}.txt"
if args.part == 1:
    # Part 1
    total = 0
    with open(file_name, "r") as f:
        lines = f.readlines()
    for line in lines:
        name = line.split(":")[0]
        numbers = line.split(":")[1]
        winning = [int(x) for x in numbers.split("|")[0].split()]
        found = [int(x) for x in numbers.split("|")[1].split()]
        card = 0
        for n in found:
            if n in winning:
                card += 1
        if card > 0:
            total += pow(2, card-1)
    print(total)
        
if args.part == 2:
    # Part 2
    total = 0
    with open(file_name, "r") as f:
        lines = f.readlines()
    instances = [1]*len(lines)
    for idx, line in enumerate(lines):
        name = line.split(":")[0]
        numbers = line.split(":")[1]
        winning = [int(x) for x in numbers.split("|")[0].split()]
        found = [int(x) for x in numbers.split("|")[1].split()]
        card = 0
        for n in found:
            if n in winning:
                card += 1
        if card > 0:
            for x in range(card):
                instances[idx+x+1] += instances[idx]
    print(sum(instances))
    