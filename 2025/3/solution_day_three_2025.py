import pathlib
import sys


def get_input(file_name: str = "input.txt") -> list[str]:
    with open(pathlib.Path(sys.path[0], file_name)) as f:
        data = f.readlines()
    return [line.rstrip() for line in data]

def solve(input: str, need: int) -> int:
    accum = 0
    for bank in input:
        string = ''
        start = 0
        found_count = 0
        while found_count < need:
            remaining = need - found_count   
            highest = 0
            highest_idx = 0
            for j in range(start, len(bank) - (remaining - 1)):
                if int(bank[j]) > highest:
                    highest = int(bank[j])
                    highest_idx = j
            
            string += str(highest)
            found_count += 1
            start = highest_idx + 1

        accum += int(string)

    return accum

def solution_part_one(input: str) -> int:
    return solve(input, 2)

def solution_part_two(input: str) -> int:
    return solve(input, 12)


if __name__ == "__main__":
    input = get_input("input.txt")
    print(solution_part_one(input))
    print(solution_part_two(input))