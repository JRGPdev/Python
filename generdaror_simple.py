def my_generator():
    yield 1
    yield 2
    yield 3
    
for value in my_generator():
    print(value)
    
#Fibonacci
# 0 1 1 2 3 5 8 13 21...
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
        
for num in fibonacci(10):
    print(num)
    
#Generador de numeros pares
def even_numbers(limit):
    for i in range(0, limit+1, 2):
        yield i

for num in even_numbers(10):
    print(num)