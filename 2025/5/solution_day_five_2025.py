import pathlib
from re import split
import sys
from unittest.util import strclass


def get_input(file_name: str = "input.txt") -> list[str]:
    with open(pathlib.Path(sys.path[0], file_name)) as f:
        data = f.readlines()
    return [line.rstrip() for line in data]

def split_input(input: list[str]) -> tuple[list[str], list[str]]:
    divider = 0
    for i in range(len(input)):
        if input[i] == '':
            divider = i
            break
    return input[:divider], input[divider + 1:]


def in_range(r: str, num: str) -> bool:
    low = int(r.split("-")[0])
    high = int(r.split("-")[1])
    if int(num) <= high and int(num) >= low:
        return True
    return False


def solution_part_one(input: list[str]) -> int:
    fresh_ranges, avail_ids = split_input(input)

    fresh_count = 0
    for id in avail_ids:
        for r in fresh_ranges:
            if in_range(r, id):
                fresh_count += 1
                break

    return fresh_count

def solution_part_two(input: str) -> int:
    pass


if __name__ == "__main__":
    input = get_input("input.txt")
    print(solution_part_one(input))
    print(solution_part_two(input))