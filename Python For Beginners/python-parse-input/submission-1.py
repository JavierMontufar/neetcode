from typing import List

def read_integers() -> List[int]:
    # nums = []
    # for num in input().split(","):
    #     nums.append(int(num))
    # return nums
    return [int(num) for num in input().split(",")]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
