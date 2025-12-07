import pathlib
import sys
import copy

PAPER = "@"
EMPTY = "."

def get_input(file_name: str = "input.txt") -> list[str]:
    with open(pathlib.Path(sys.path[0], file_name)) as f:
        data = f.readlines()
    return [line.rstrip() for line in data]


def solution_part_one(input: list[str]) -> int:
    accum = 0
    height = len(input)
    width = len(input[0])

    for row_idx, line in enumerate(input):
        for col_idx, spot in enumerate(line):
            # Are we on an @?
            if spot == PAPER:
                count = 0
                
                # Check left
                if col_idx != 0: # Bounds check
                    if line[col_idx - 1] == PAPER:
                        count += 1
                
                # Check above
                if row_idx != 0: # Bounds check
                    if input[row_idx - 1][col_idx] == PAPER:
                        count += 1

                # Check above and left
                if row_idx != 0 and col_idx != 0: # Bounds check
                    if input[row_idx - 1][col_idx - 1] == PAPER:
                        count += 1

                # Check right
                if col_idx != width - 1: # Bounds check
                    if line[col_idx + 1] == PAPER:
                        count += 1

                # Check above and right
                if row_idx != 0 and col_idx != width - 1: # Bounds check
                    if input[row_idx - 1][col_idx + 1] == PAPER:
                        count += 1

                # Check below
                if row_idx != height - 1: # Bounds check
                    if input[row_idx + 1][col_idx] == PAPER:
                        count += 1

                # Check below and left
                if row_idx != height - 1 and col_idx != 0: # Bounds check
                    if input[row_idx + 1][col_idx - 1] == PAPER:
                        count += 1

                # Check below and right
                if row_idx != height - 1 and col_idx != width - 1: # Bounds check
                    if input[row_idx + 1][col_idx + 1] == PAPER:
                        count += 1

                # If there were 3 or fewer rolls of paper?
                if count <= 3:
                    accum += 1

    return accum

def alg(input: list[str]) -> (int, list[str]):
    accum = 0
    height = len(input)
    width = len(input[0])
    input_copy = copy.deepcopy(input)

    for row_idx, line in enumerate(input):
        for col_idx, spot in enumerate(line):
            # Are we on an @?
            if spot == PAPER:
                count = 0
                
                # Check left
                if col_idx != 0: # Bounds check
                    if line[col_idx - 1] == PAPER:
                        count += 1
                
                # Check above
                if row_idx != 0: # Bounds check
                    if input[row_idx - 1][col_idx] == PAPER:
                        count += 1

                # Check above and left
                if row_idx != 0 and col_idx != 0: # Bounds check
                    if input[row_idx - 1][col_idx - 1] == PAPER:
                        count += 1

                # Check right
                if col_idx != width - 1: # Bounds check
                    if line[col_idx + 1] == PAPER:
                        count += 1

                # Check above and right
                if row_idx != 0 and col_idx != width - 1: # Bounds check
                    if input[row_idx - 1][col_idx + 1] == PAPER:
                        count += 1

                # Check below
                if row_idx != height - 1: # Bounds check
                    if input[row_idx + 1][col_idx] == PAPER:
                        count += 1

                # Check below and left
                if row_idx != height - 1 and col_idx != 0: # Bounds check
                    if input[row_idx + 1][col_idx - 1] == PAPER:
                        count += 1

                # Check below and right
                if row_idx != height - 1 and col_idx != width - 1: # Bounds check
                    if input[row_idx + 1][col_idx + 1] == PAPER:
                        count += 1

                # If there were 3 or fewer rolls of paper?
                if count <= 3:
                    accum += 1
                    row = input_copy[row_idx]
                    input_copy[row_idx] = row[:col_idx] + EMPTY + row[col_idx + 1:]

    return accum, input_copy

def solution_part_two(input: str) -> int:
    total = 0
    while True:
        accum, input = alg(input)
        total += accum
        if accum == 0:
            break

    return total


if __name__ == "__main__":
    input = get_input("input.txt")
    print(solution_part_one(input))
    print(solution_part_two(input))