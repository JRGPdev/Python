import csv


#leer un archivo 
""" with open('lectura y escritura\products.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row) """
        
#mostrar la informacion por columnas
with open('lectura y escritura\products.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")