'''
Explicación rápida

Representación: el tablero se representa con una lista reinas, donde el índice es la fila y el valor es la columna donde está la reina.
Ejemplo: reinas = [1, 3, 0, 2] significa que en fila 0 está en col 1, fila 1 en col 3, etc.

Seguridad (es_seguro): se revisa que no haya otra reina en la misma columna o en diagonales.

Backtracking (backtrack): coloca reinas fila por fila, retrocede si no encuentra posición válida.

Resultados: imprime todas las soluciones con un tablero visual de Q y ..
'''

def imprimir_tablero(tablero, N):
    """Imprime el tablero en formato visual."""
    for fila in tablero:
        linea = ""
        for col in range(N):
            if col == fila:
                linea += " Q "
            else:
                linea += " . "
        print(linea)
    print("\n")


def es_seguro(reinas, fila, col):
    """Verifica si se puede colocar una reina en (fila, col)."""
    for i in range(fila):
        if reinas[i] == col or \
           reinas[i] - i == col - fila or \
           reinas[i] + i == col + fila:
            return False
    return True


def resolver_n_reinas(N):
    """Resuelve el problema de las N-Reinas y devuelve todas las soluciones."""
    soluciones = []
    reinas = [-1] * N

    def backtrack(fila):
        if fila == N:
            soluciones.append(reinas[:])
            return
        for col in range(N):
            if es_seguro(reinas, fila, col):
                reinas[fila] = col
                backtrack(fila + 1)
                reinas[fila] = -1

    backtrack(0)
    return soluciones


if __name__ == "__main__":
    N = int(input("Introduce el valor de N (tamaño del tablero): "))
    soluciones = resolver_n_reinas(N)
    print(f"Se encontraron {len(soluciones)} soluciones para {N}-Reinas.\n")

    for idx, sol in enumerate(soluciones, 1):
        print(f"Solución {idx}:")
        imprimir_tablero(sol, N)
