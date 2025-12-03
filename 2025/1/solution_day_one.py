import pathlib
import sys


def get_input(file_name: str = "input.txt") -> list[str]:
    with open(pathlib.Path(sys.path[0], file_name)) as f:
        data = f.readlines()
    return [line.rstrip() for line in data]

class Dial:
    def __init__(self) -> None:
        self._position = 50
        self._zero_count = 0
            
    def forward(self, number: int = 1) -> None:
        for i in range(number):
            if self._position == 99:
                self._position = 0
            else:
                self._position += 1
                
            if self._position == 0:
                self._zero_count += 1

    def reverse(self, number: int = 1) -> None:
        for i in range(number):
            if self._position == 0:
                self._position = 99
            else: 
                self._position -= 1
                
            if self._position == 0:
                self._zero_count += 1
                            
    @property
    def position(self) -> int:
        return self._position
    
    @property
    def zero_count(self) -> int:
        return self._zero_count
    
def solution_part_one(input: list[str]) -> int:
    d = Dial()
    num_of_zeros: int = 0
    for instruction in input:
        if instruction.startswith("R"):
            amt = int(instruction.split("R")[1])
            d.forward(amt)
        if instruction.startswith("L"):
            amt = int(instruction.split("L")[1])
            d.reverse(amt)
            
        if d.position == 0:
            num_of_zeros += 1
        
    return num_of_zeros

def solution_part_two(input: list[str]) -> int:
    d = Dial()
    for instruction in input:
        if instruction.startswith("R"):
            amt = int(instruction.split("R")[1])
            d.forward(amt)
        if instruction.startswith("L"):
            amt = int(instruction.split("L")[1])
            d.reverse(amt)
        
    return d.zero_count

if __name__ == "__main__":
    input = get_input()
    print(solution_part_one(input))
    print(solution_part_two(input))