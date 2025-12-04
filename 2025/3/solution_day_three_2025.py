from itertools import product
import pathlib
import sys


def get_input(file_name: str = "input.txt") -> list[str]:
    with open(pathlib.Path(sys.path[0], file_name)) as f:
        data = f.readlines()
    return [line.rstrip() for line in data]


def solution_part_one(input: str) -> int:
    accum = 0
    for bank in input:
        highest = 0
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                num = int(bank[i]+bank[j])
                if num > highest:
                    highest = num

        accum += highest

    return accum

def solution_part_two(input: str) -> int:
    pass


if __name__ == "__main__":
    input = get_input("input.txt")
    print(solution_part_one(input))
    # print(solution_part_two(input))