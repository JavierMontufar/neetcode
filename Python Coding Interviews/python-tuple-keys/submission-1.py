from typing import List, Set, Tuple


def grid_to_set(grid: List[List[int]]) -> Set[Tuple[int, int]]:
    # my_set = set()
    # for row, sublist in enumerate(grid):
    #     for col, el in enumerate(sublist):
    #         if el == 1:
    #             my_set.add((row, col))
    # return my_set

    return {
        (row, col) 
        for row, sublist in enumerate(grid)
        for col, el in enumerate(sublist)
        if el==1}


# do not modify below this line

output1 = grid_to_set([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(type(output1))
print(sorted(list(output1)))
      
output2 = grid_to_set([[1, 0, 0], [0, 0, 0]])
print(type(output2))
print(sorted(list(output2)))

output3 = grid_to_set([[1, 1, 1], [1, 1, 1]])
print(type(output3))
print(sorted(list(output3)))

output4 = grid_to_set([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(type(output4))
print(sorted(list(output4)))
