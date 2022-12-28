from time import sleep

MATRIZ_DEFAULT = [[0, 1, 0], [1, 0, 1], [0, 0, 1]]

def checa_irmao(matriz, x, y):
    lado = 0 if matriz[x][y] == 0 else -1
    for j in range(-1, 2):
        for i in range(-1, 2):
            aux_x = x + j
            aux_y = y + i
            if (aux_x >= 0 and aux_y >= 0) and (aux_x < len(matriz) and aux_y < len(matriz[0])):
                lado += matriz[aux_x][aux_y]
    return lado

def printa_matriz(matriz):
    for l in matriz:
        for c in l:
            print("0 " if c == 0 else "# ", end='')
        print()
    print("-------------------")

def atualiza_matriz(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            irmao = checa_irmao(matriz, linha, coluna)
            matriz[linha][coluna] = int(
                (matriz[linha][coluna] == 0 and irmao == 3)
                or (matriz[linha][coluna] == 1 and (not (irmao < 2 or irmao > 3)))
            )
    return matriz


def main():
    matriz = MATRIZ_DEFAULT
    try:
        while True:
            printa_matriz(matriz)
            matriz = atualiza_matriz(matriz)
            sleep(1)
    except KeyboardInterrupt:
        print('fechou!')


if __name__ == '__main__':
    main()