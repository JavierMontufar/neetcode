class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []

        actualMxL = 0
        for i, h in enumerate(height):
            maxLeft.append(actualMxL)
            if h > actualMxL:
                actualMxL = h

        height.reverse()

        actualMxR = 0 
        for i, h in enumerate(height):
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
            if area > 0:
                res.append(area)
            else:
                res.append(0)
        
        return sum(res)

        