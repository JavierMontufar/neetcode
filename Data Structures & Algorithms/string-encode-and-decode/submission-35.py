class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for string in strs:
            longitud = str(len(string))  # convierte la longitud a cadena
            encodedStr += longitud + "#" + string
        return encodedStr

    def decode(self, s: str) -> List[str]:
        print(s)
        numeroStr = ""
        output = []
        i = 0
        while i < len(s):
            caracter = s[i] #extraemos el caracter s[i] que recorre todo el arreglo s
            #si el caracter es "#" convertimos el numero en entero
            if caracter in "#":
                numero = int(numeroStr)
                #tomamos los siguentes numero caracteres de s mas 1 para evitar el "#"
                palabra = ""+str(s[i+1:i+numero+1])
                #agregamos la palabra al output
                output.append(palabra)
                #sumamos el numero de caracteres que de la cadena al inidice i para no tomarlos en cuenta
                i += numero
                #inicializamos numeroStr a cadena vacia nuevamente
                numeroStr = ""
            #si el caracter es un numero lo convertimos a string y lo concatenamos a numeroStr
            elif caracter in "0123456789":
                numeroStr += str(caracter)
            #avanzamos en el contador de i
            i+= 1
        return output
