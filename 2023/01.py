# Part 1
import re
nums = []
with open("01-1.txt", "r") as f:
    lines = f.readlines()
for line in lines:
    n = re.findall(r"\d", line)
    nums.append(int(f"{n[0]}{n[-1]}"))
print(sum(nums))
# Part 2
nums = []
with open("01-1.txt", "r") as f:
    lines = f.readlines()
numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
for line in lines:
    lnum = []
    for idx in range(len(line)):
        if line[idx].isdigit():
            lnum.append(int(line[idx]))
        else:
            for k, v in numbers.items():
                if idx+len(k) < len(line) and line[idx:idx+len(k)] == k:
                    lnum.append(v)
    nums.append(10*lnum[0] + lnum[-1])
print(sum(nums))

