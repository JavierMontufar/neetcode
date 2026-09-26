class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        result = []

        def traverse_spiral(top_row, right_column, bottom_row, left_column):
            if top_row > bottom_row:
                return
            
            if right_column < left_column:
                return

            # fist loop tarverse top_row from 0 to right_column
            result.extend(matrix[top_row][left_column:right_column+1])

            #second loop travers top to bottom alog the right column
            # fijo right column
            for i in range(top_row+1, bottom_row+1):
                result.append(matrix[i][right_column])
            
            #third loop travers right to left along the bottom_row
            if top_row < bottom_row:
                for i in range(right_column - 1, left_column - 1, -1):
                    result.append(matrix[bottom_row][i])
            
            #fourth loop travers bottom to top along the left_columns
            if left_column < right_column:
                for i in range(bottom_row-1, top_row, -1):
                    result.append(matrix[i][left_column])

            traverse_spiral(top_row+1, right_column-1, bottom_row-1, left_column+1)

        # initial conditions

        top_row = 0
        right_column = len(matrix[0])-1
        bottom_row = len(matrix)-1
        left_column = 0

        traverse_spiral(top_row, right_column, bottom_row, left_column)

        return result
