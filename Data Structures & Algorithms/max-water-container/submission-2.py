class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #un puntero de principio y de fin
        start, end = 0, len(heights)-1
        #cantidad de agua
        amount_water = 0
        #mientras el fin sea mayor al inicio
        while end > start:
            #calculamos la cantidad de agua
            amount_water = max(amount_water, (end-start) * min(heights[start], heights[end]))
            #si la altura de start es mayor a altura end
            if heights[start] < heights[end]:
                #movemos start
                start += 1
            #si la altura de end es mayor a start
            elif heights[end] < heights[start]:
                #movemos end
                end -= 1
            #si son iguales movemos los dos
            else:
                start += 1
                end -= 1
        #regresamos la cantidad de agua
        return amount_water
        