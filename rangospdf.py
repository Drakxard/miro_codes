#python rangospdf.py name.pdf inicio fin
import sys
import os
from PyPDF2 import PdfReader, PdfWriter

def generar_nombre(base="tema", ext=".pdf"):
    n = 1
    while os.path.exists(f"{base}_{n}{ext}"):
        n += 1
    return f"{base}_{n}{ext}"

def extraer_paginas(pdf_path, inicio, fin):
    try:
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        # Validación
        total = len(reader.pages)
        if inicio < 1 or fin > total or inicio > fin:
            print(f"Rango inválido. PDF tiene {total} páginas.")
            return

        for i in range(inicio - 1, fin):  # PyPDF2 usa índice 0
            writer.add_page(reader.pages[i])

        salida = generar_nombre()
        with open(salida, "wb") as f:
            writer.write(f)
        print(f"Archivo generado: {salida}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python extraer_pdf.py archivo.pdf pagina_inicio pagina_fin")
    else:
        archivo = sys.argv[1]
        inicio = int(sys.argv[2])
        fin = int(sys.argv[3])
        extraer_paginas(archivo, inicio, fin)
