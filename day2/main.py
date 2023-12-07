import re
import math
from collections import defaultdict

def sum_of_game_ids(games):
    ids = 0
    total_power = 0
    for g in games:
        parts = re.sub("[;,:]", "", g).split()
        max_cubes = defaultdict(int)
        for count, color in zip(parts[2::2], parts[3::2]):
            max_cubes[color] = max(max_cubes[color], int(count))
        if max_cubes["red"] <= 12 and max_cubes["green"] <= 13 and max_cubes["blue"] <= 14:
            ids += int(parts[1]) 
        total_power += math.prod(max_cubes.values())
    print(ids)
    print(total_power)


with open("day2/input.txt") as file:
    games = file.readlines()


print(sum_of_game_ids(games))

