class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts1 = {}
        counts2_window = {}
        window_length = len(s1)

        # Contamos el número de cada caracter en s1
        for char in s1:
            counts1[char] = counts1.get(char, 0) + 1

        # Contamos el número de cada caracter en la primera ventana se s2
        for i in range(window_length):
            char = s2[i]
            counts2_window[char] = counts2_window.get(char, 0) + 1

        # Comparamos la primera ventana de s2
        if counts1 == counts2_window:
            return True

        # Recorremos s2 con una ventana deslizante
        for i in range(window_length, len(s2)):
            # El carácter que sale de la ventana
            left_char = s2[i - window_length]
            counts2_window[left_char] -= 1
            if counts2_window[left_char] == 0:
                del counts2_window[left_char]

            # El nuevo carácter que entra a la ventana
            right_char = s2[i]
            counts2_window[right_char] = counts2_window.get(right_char, 0) + 1

            # Comparamos los conteos
            if counts1 == counts2_window:
                return True

        return False
