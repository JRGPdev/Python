#ejemplo de iterador

#crear un iterador
my_list=[1,2,3,4,5]

#obtener un iterador
my_iter=iter(my_list)

#usar iterador
#next ayuda a ver los datos que se estan almacenando en el iterador en memoria
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#iterador de texto en cadena
#creando la cadena
text="Hola mundo"
#creando el objeto iterador
iter_text=iter(text)

#iterar en la cadena
for char in iter_text:
    print(char)
    
    
#crear un iterador para los numeros impares

#limite
limit=10
#crear un iterador
add_itter = iter(range(1,limit+1,2))

#usar un iterador
for num in add_itter:
    print(num)