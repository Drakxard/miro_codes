#!/usr/bin/env python3
"""
intervalo.py

Este script toma una serie de números enteros como argumentos de línea de comandos
y genera una lista de intervalos:

- Para cada par adyacente `a[i]` y `a[i+1]`, crea un intervalo.
- El extremo superior de cada intervalo siempre será `a[i+1] - 1`.

Ejemplo:
    python intervalo.py 1 4 7
    -> (1, 3)
       (4, 6)

"""
import sys

def crear_intervalos(a):
    """
    Recibe una lista de enteros `a` y devuelve una lista de tuplas (start, end):
      - start = a[i]
      - end = a[i+1] - 1
    """
    return [(a[i], a[i+1] - 1) for i in range(len(a) - 1)]


def main():
    # Verificar al menos dos números
    if len(sys.argv) < 3:
        sys.stderr.write("Uso: python intervalo.py num1 num2 [...]")
        sys.exit(1)

    # Parseo de argumentos
    try:
        nums = [int(arg) for arg in sys.argv[1:]]
    except ValueError:
        sys.stderr.write("Error: Todos los argumentos deben ser enteros.\n")
        sys.exit(1)

    # Generar e imprimir intervalos
    for start, end in crear_intervalos(nums):
        print(f"({start}, {end})")


if __name__ == "__main__":
    main()
