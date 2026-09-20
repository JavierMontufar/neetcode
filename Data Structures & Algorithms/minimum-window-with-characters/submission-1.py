class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {}, {}

        #Inicializamos el has map de c
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        #Inicilizamos have a 0 y ned al numero de caracteres de counT. Res es -1 y resLen infinity. l y r empiezan en 0
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        #Recorremos con una ventana
        for r in range(len(s)):

            #Aumentamos en uno la cuenta del carcater actual en hashmap
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            #Actualizamos have en uno si c esta en couunT y el numero de caracteres es el mismo
            if c in countT and window[c] == countT[c]:
                have += 1
            
            #Mientras have sea igual a ned vamos a actualizar el resultado si es menor a la longitud actual
            #y vamos a actualizar la ventana quitando de la izquierda caracteres
            while have == need:
                #update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                #pop from the left
                window[s[l]] -= 1
                #recuerda que al quitar de la izquierda si la cuenta ya es menor, tenemos que reducir have en uno
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        #regresamos el pointer de left (l) a right (r)
        return s[l:r+1] if resLen != float("infinity") else ""


        