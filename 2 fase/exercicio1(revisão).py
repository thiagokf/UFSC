class Ordenacao():

    def ordena(self, array_para_ordenar:[]):
        t = len(array_para_ordenar)
        for i in range(t):
            for j in range(0, t-i-1):
                if array_para_ordenar[j] > array_para_ordenar[j+1]:
                    array_para_ordenar[j], array_para_ordenar[j+1] = array_para_ordenar[j+1], array_para_ordenar[j]
                

        return array_para_ordenar

    def to_string(self, array_ordenado:[]):
        string = ','.join(str(numero) for numero in array_ordenado)
        
        return string
