class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        color_original = image[sr][sc]

        if image[sr][sc] == color:
            return image
        
        def cambiar_color(fila,columna):
            if (fila < 0 or fila >= len(image)) or (columna < 0 or columna >= len(image[0])):
                return
            
            if image[fila][columna] != color_original:
                return
            
            image[fila][columna] = color

            # cambiar color a la izquierda
            cambiar_color(fila-1, columna) 
            # cambiar color arriba
            cambiar_color(fila, columna-1) 
            # cambiar color a la derecha
            cambiar_color(fila+1, columna) 
            # cambiar color abajo
            cambiar_color(fila, columna+1) 

        

        cambiar_color(sr,sc)
        return image