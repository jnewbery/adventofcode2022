#!/usr/bin/env python3
from dataclasses import dataclass
import functools
import json

from utils import get_params, exit_not_implemented, time_execution

@dataclass
class Hand:
    red: int=0
    green: int=0
    blue: int=0

    def contains(self, other: 'Hand') -> bool:
        return self.red >= other.red and self.green >= other.green and self.blue >= other.blue

    @classmethod
    def from_txt(cls, line: str) -> 'Hand':
        red, green, blue = 0, 0, 0
        cubes_strs = line.split(',')
        for color_str in cubes_strs:
            num, color = color_str.split()
            if color == 'red':
                red = int(num)
            elif color == 'green':
                green = int(num)
            elif color == 'blue':
                blue = int(num)
        return cls(red, green, blue)

    def merge(self, other: 'Hand') -> 'Hand':
        return Hand(max(self.red, other.red), max(self.green, other.green), max(self.blue, other.blue))

    def power(self) -> int:
        return self.red * self.green * self.blue

MAX_HAND = Hand(12, 13, 14)

def play_game(line: str) -> bool:
    line = line.split(':')[1].strip()
    # print(line)
    return functools.reduce(lambda x, y: x.merge(y), [Hand.from_txt(hand) for hand in line.split(';')]).power()
    # for hand in line.split(';'):
        # if not MAX_HAND.contains(Hand.from_txt(hand)):
            # return False
    # return True

# def main():
#     file_name = 'input2.txt'
#     ret = 0
#     with open(file_name) as f:
#         # print(sum(ix + 1 for ix, game in enumerate(f.readlines()) if play_game(game)))
#         print(sum(play_game(game) for game in f.readlines()))
#         # for ix, game in enumerate(f.readlines()):
#             # print(play_game(game))
#             # if play_game(game):
#                 # print(f'Game {ix + 1} is {play_game(game)}')
#                 # ret += ix + 1
#     print(ret)

@time_execution
def part1(ll):
    exit_not_implemented()

@time_execution
def part2(ll):
    return sum(play_game(game) for game in ll)

if __name__ == "__main__":
    args = get_params(__file__)

    if args.part == "1":
        sol = part1(args.puzzle_input.splitlines())
    elif args.part == "2":
        sol = part2(args.puzzle_input.splitlines())

    if args.verbose:
        print(json.dumps(sol))
    else:
        print(sol["solution"])
