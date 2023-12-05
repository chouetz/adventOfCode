import argparse

parser = argparse.ArgumentParser()
parser.add_argument("part", help="game part", type=int)
parser.add_argument("-t", "--test", action="store_true")
args = parser.parse_args()
test = f"-{args.part}-test" if args.test else ""
file_name = f"{__file__.split('/')[-1].split('.')[0]}{test}.txt"
if args.part == 1:
    # Part 1
    with open("02-1.txt", "r") as f:
        lines = f.readlines()
    limits = {"red": 12, "green": 13, "blue": 14}
    games = 0
    for line in lines:
        game, picks = line.split(":")
        discard = False
        for pick in picks.split(";"):
            for colors in pick.split(","):
                num, color = colors.split()
                if int(num) > limits[color]:
                    discard = True
        if not discard:
            games += int(game.split()[1])
    print(games)
if args.part == 2:
    # Part 2
    with open(file_name, "r") as f:
        lines = f.readlines()
    powers = []
    for line in lines:
        game, picks = line.split(":")
        maxs = {"red": 0, "green": 0, "blue": 0}
        discard = False
        for pick in picks.split(";"):
            for colors in pick.split(","):
                num, color = colors.split()
                if int(num) > maxs[color]:
                    maxs[color] = int(num)
        powers.append(maxs["blue"] * maxs["green"] * maxs["red"])
    print(sum(powers))
    