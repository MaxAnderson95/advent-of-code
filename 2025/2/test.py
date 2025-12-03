from solution import get_input, solution_part_one, solution_part_two

input = get_input()

def test_solution_part_one() -> None:
    assert solution_part_one(input) == 13108371860


def test_solution_part_two() -> None:
    assert solution_part_two(input) == 22471660255


if __name__ == "__main__":
    test_solution_part_one()
    test_solution_part_two()