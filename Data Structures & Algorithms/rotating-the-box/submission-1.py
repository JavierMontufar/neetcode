class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])


        for row in range(rows):
            i = cols-1
            for c in reversed(range(cols)):
                if boxGrid[row][c] == "#":
                    boxGrid[row][c], boxGrid[row][i] = boxGrid[row][i], boxGrid[row][c]
                    i -= 1
                
                elif boxGrid[row][c] == "*":
                    i = c-1
        result = []

        for j in range(cols):
            row_result = []
            for i in reversed(range(rows)):
                row_result.append(boxGrid[i][j])
            result.append(row_result)
        
        return result