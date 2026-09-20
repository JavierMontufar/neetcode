class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        output = []

        #recorremos el arreglo nums con el indice i
        while i < len(nums):
            #inicializamos mult en 1 y el indice j en 0
            mult = 1
            j = 0

            #recorremos nuevamente nums con j
            while j < len(nums):
                #si i es diferente de j hacemos la mult de mult * nums[j]
                if(i != j):
                    mult *= nums[j]
                j += 1
            #al arreglo output le añadimos el resultado de mult
            output.append(mult)
            i += 1
        #regresamos output
        return output