#leer un archivo linea por linea
""" with open('lectura y escritura\caperucita.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip()) """
        
#leer todas las lineas en una lista
""" with open('lectura y escritura\caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines) """
    
#añadir una linea al final del archivo
""" with open('lectura y escritura\caperucita.txt', 'a') as file:
    file.write("\n\nJose Rene") """
    
#sobreescribir un archivo
""" with open('lectura y escritura\caperucita.txt', 'w') as file:
    file.write("\n\nJose Rene") """
    
#conteos de lineas
with open('lectura y escritura\caperucita.txt', 'r') as file:
    file_lines = file.readlines()
    print(f"El archivo tiene {len(file_lines)} lineas")