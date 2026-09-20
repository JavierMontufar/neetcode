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

        i=0
        while i < len(s):
            caracter = s[i]
            if caracter in "#":
                if numeroStr != '':
                    numero = int(numeroStr)
                    #tomamos los siguentes numero caracteres de s
                    palabra = ""+str(s[i+1:i+numero+1])
                    output.append(palabra)
                    i += numero
                    numeroStr = ""
            elif caracter in "0123456789":
                numeroStr += str(caracter)
            print("i "+str(i))
            print("numeroStr "+numeroStr)
            print(output)
            i+= 1
        return output
