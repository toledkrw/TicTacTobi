def avaliar_horizontal(matrix):
    for i in range(3):
        if(matrix[i][0] == matrix[i][1] and matrix[i][1] == matrix[i][2] and matrix[i][0] != " "):
            return True
    return False

def avaliar_vertical(matrix):
    for i in range(3):
        if(matrix[0][i] == matrix[1][i] and matrix[1][i] == matrix[2][i] and matrix[0][i] != " "):
            return True
    return False

def avaliar_diagonal(matrix):
    if(matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] and matrix[0][0] != " "):
        return True
    if(matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0] and matrix[0][2] != " "):
        return True
    return False


def avaliar_vencedor(matrix):
    #avaliar horizontal
    if(avaliar_horizontal(matrix)):
        return "horizontal"
    
    if(avaliar_vertical(matrix)):
        return "vertical"
    
    if(avaliar_diagonal(matrix)):
        return "diagonal"



input = "o:2,2 x:2,1 o:3,3 x:1,1 o:3,1 x:1,3 o:3,2"
list_ = input.split(" ")

matrix = [[" "," "," "], [" "," "," "], [" "," "," "]]


for jogada in list_:
    if "x" in jogada:
        dados = jogada.split(":")
        dados = dados[1].split(",")
        matrix[int(dados[0]) - 1][int(dados[1]) - 1] = "x"
        
    if "o" in jogada:
        dados = jogada.split(":")
        dados = dados[1].split(",")
        matrix[int(dados[0]) - 1][int(dados[1]) - 1] = "o"


print(matrix)
print(f"Houve um vencedor na: {avaliar_vencedor(matrix)}")