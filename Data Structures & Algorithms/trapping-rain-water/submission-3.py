class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []

        actualMxL = 0
        for h in height:
            maxLeft.append(actualMxL)
            if h > actualMxL:
                actualMxL = h

        height.reverse()

        actualMxR = 0 
        for h in height:
            maxRight.append(actualMxR)
            if h > actualMxR:
                actualMxR = h
        
        height.reverse()
        maxRight.reverse()

        minLR = []
        for i in range(len(height)):
            minLR.append(min(maxLeft[i], maxRight[i]))

        res = []
        for i, h in enumerate(height):
            area = minLR[i] - h
            res.append(area if area > 0 else 0)
        
        return sum(res)

        