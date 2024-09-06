import json

#lectura del archivo
with open('Python\lectura y escritura\products.json') as file:
    products = json.load(file)
    
#mostrar el contenido
for product in products:
    #print(product)
    print(f"Proudct: {product['name']}, price: {product['price']}")