import os

#obtener el directorio actual
""" cwd = os.getcwd()
print("Directorio actual:", cwd) """

#listar los archivos .txt
""" txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos .txt:", txt_files) """

#renombrar
os.rename('archivo.txt', 'archivo_renombrado.txt')
print("Archivo renombrado")             