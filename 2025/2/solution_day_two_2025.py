from itertools import product
import pathlib
import sys


def get_input(file_name: str = "input.txt") -> str:
    with open(pathlib.Path(sys.path[0], file_name)) as f:
        data = f.readlines()
    return data[0]


def solution_part_one(input: str) -> int:
    bad_product_ids: list[int] = []

    for product_range in input.split(","):
        start = int(product_range.split("-")[0])
        end = int(product_range.split("-")[1])
        
        # If the start AND end's lengths are odd, we can skip the whole range
        if len(str(start)) % 2 != 0 and len(str(end)) % 2 != 0:
            continue

        # Loop through the range of numbers including the last number
        for i in range(start, end + 1):
            # If i's length is odd (we're in a mixed length range), we can skip it
            if len(str(i)) % 2 != 0:
                continue

            # Split the number in half by length and see if the first and second half are the same
            length = len(str(i))
            half_length = int(length/2)
            first_half = str(i)[:half_length]
            second_half = str(i)[half_length:]

            # If they match add them to the list of bad product ids
            if first_half == second_half:
                bad_product_ids.append(i)

    # Sum all of the product ids
    return sum(bad_product_ids)

def solution_part_two(input: str) -> int:
    bad_product_ids: list[int] = []

    for product_range in input.split(","):
        start = int(product_range.split("-")[0])
        end = int(product_range.split("-")[1])

        # Loop through the range of numbers including the last number
        for i in range(start, end + 1):
            length = len(str(i))
            
            match length:
                # Handle all of the prime number lengths to see if 
                # divided into half, 3rds, 5ths, 7th, etc 
                # i.e. they are all the same number (ex. 1111111)
                case 2 | 3 | 5 | 7 | 11:
                    if len(set(str(i))) == 1:
                        bad_product_ids.append(i)

                case 4:
                    if len(set(str(i))) == 1:
                        bad_product_ids.append(i)
                    # Split in half
                    elif str(i)[:2] == str(i)[-2:]:
                        bad_product_ids.append(i)

                case 6:
                    if len(set(str(i))) == 1:
                        bad_product_ids.append(i)
                    # Split in half
                    elif str(i)[:3] == str(i)[-3:]:
                        bad_product_ids.append(i)
                    # Split in 3rds
                    elif str(i)[:2] == str(i)[2:4] == str(i)[-2:]:
                        bad_product_ids.append(i)

                case 8:
                    if len(set(str(i))) == 1:
                        bad_product_ids.append(i)
                    # Split in half
                    elif str(i)[:4] == str(i)[-4:]:
                        bad_product_ids.append(i)
                    # Split in 4ths
                    elif str(i)[:2] == str(i)[2:4] == str(i)[4:6] == str(i)[-2:]:
                        bad_product_ids.append(i)

                case 9:
                    if len(set(str(i))) == 1:
                        bad_product_ids.append(i)
                    # Split in 3rds
                    elif str(i)[:3] == str(i)[3:6] == str(i)[-3:]:
                        bad_product_ids.append(i)

                case 10:
                    if len(set(str(i))) == 1:
                        bad_product_ids.append(i)
                    # Split in half
                    elif str(i)[:5] == str(i)[-5:]:
                        bad_product_ids.append(i)
                    # Split in 5ths
                    elif str(i)[:2] == str(i)[2:4] == str(i)[4:6] == str(i)[6:8] == str(i)[-2:]:
                        bad_product_ids.append(i)

    return sum(bad_product_ids)

if __name__ == "__main__":
    input = get_input("input.txt")
    print(solution_part_one(input))
    print(solution_part_two(input))