class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        maxLeft = []
        maxRight = []

        # Calcular máximos por la izquierda
        actualMxL = 0
        for h in height:
            maxLeft.append(actualMxL)
            if h > actualMxL:
                actualMxL = h

        # Calcular máximos por la derecha
        actualMxR = 0
        for h in reversed(height):
            maxRight.append(actualMxR)
            if h > actualMxR:
                actualMxR = h

        # Invertir lista maxRight para emparejar índices
        maxRight.reverse()

        # Tomar el mínimo entre maxLeft y maxRight
        minLR = []
        for i in range(len(height)):
            minLR.append(min(maxLeft[i], maxRight[i]))

        # Calcular agua atrapada
        res = []
        for i, h in enumerate(height):
            area = minLR[i] - h
            if area > 0:
                res.append(area)
            else:
                res.append(0)

        return sum(res)

        