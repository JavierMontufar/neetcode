class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []

        actualMaxL = 0
        for h in height:
            maxLeft.append(actualMaxL)
            if h > actualMaxL:
                actualMaxL = h
        
        height.reverse()
        actualMaxL = 0
        for h in height:
            maxRight.append(actualMaxL)
            if h > actualMaxL:
                actualMaxL = h
        
        maxRight.reverse()
        height.reverse()

        res = []
        for i, h in enumerate(height):
            area = min(maxLeft[i], maxRight[i]) - h
            res.append(area if area > 0 else 0)
        
        return sum(res)

        