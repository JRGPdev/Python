numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print("aqui i es igual a: ", i+1)
    
#rango de 3 a 9 solo seleeciona del 3 al 89
for i in range(3,10):
    print(i) 
    
fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
for fruta in fruits:
    if fruta == "Naranja":
        print("Naranja encontrada")

#break sirve para salir del bucle cuando se cumple una condicion   
x=0
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1
    
#continue sirve para saltar una iteracion cuando se cumple una condicion
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i == 3:
        continue
    print("aqui i es igual a: ", i)