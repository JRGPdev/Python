squares = [x**2 for x in range(1,11)]
#print("Cuadrados:", squares)

celsius = [0, 10, 20, 30, 40]
fahraneit = [((9/5)*temp + 32) for temp in celsius]
#print("temperatura en Fahrenheit:", fahraneit)

#Numeros pares
evens = [x for x in range(1, 21) if x % 2 == 0]
#print("Numeros pares:", evens)

matrix = [[1,2,3], 
          [4,5,6], 
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transposed)

# este es el código sin usar Comprehensions Lists

transposed = []
for i in range(len(matrix[0])):
    print(i)
    transposed_row = []
    for row in matrix:
        print(transposed_row)
        transposed_row.append(row[i])
    transposed.append(transposed_row)
    print(transposed_row)

print(transposed)