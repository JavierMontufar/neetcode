class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for string in strs:
            longitud = str(len(string))  # convierte la longitud a cadena
            encodedStr += longitud + "#" + string
        return encodedStr

    def decode(self, s: str) -> List[str]:
        print(s)
        numero = 0
        numeroStr = ""
        output = []

        i=0
        while i < len(s):
            caracter = s[i]
            if caracter in "#":
                if numeroStr != '':
                    numero = int(numeroStr)
                    #tomamos los siguentes numero caracteres de s
                    i += 1 #saltamos el i con "#"
                    palabra = ""+str(s[i:i+numero])
                    output.append(palabra)
                    i += numero
                    i -= 1
                    numeroStr = ""
            elif caracter in "0123456789":
                numeroStr += str(caracter)
            print("i "+str(i))
            print("numeroStr "+numeroStr)
            print(output)
            i+= 1
        return output
