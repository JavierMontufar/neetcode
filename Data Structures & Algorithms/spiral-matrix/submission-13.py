class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        result=[]

        def traverse_spiral(top_row, right_column, bottom_row, left_column):
            if bottom_row < top_row:
                return
            
            if right_column < left_column:
                return
            
            #first_loop top fijo:left->right
            result.extend(matrix[top_row][left_column:right_column+1])

            #second_loop right fijo:top+1->bottom
            for i in range(top_row+1, bottom_row+1):
                result.append(matrix[i][right_column])
            

            # third loop bottom fijo:right-1->left
            if not(top_row == bottom_row):
                # result.extend(matrix[bottom_row][right_column-1:left_column-1:-1])
                for i in range(right_column-1, left_column-1, -1):
                    result.append(matrix[bottom_row][i])

            # fourth loop left fijo:bottom-1->top+1
            if not(left_column == right_column):
                for i in range(bottom_row-1, top_row, -1):
                    result.append(matrix[i][left_column])

            traverse_spiral(top_row+1, right_column-1, bottom_row-1, left_column+1)
        



        traverse_spiral(0, len(matrix[0])-1, len(matrix)-1, 0)
        return result
