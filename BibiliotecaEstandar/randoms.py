import random

# Genera un número aleatorio 
random_number = random.randint(1, 10)
print(random_number)

#elegir colores aleatorios
colors = ['Rojo', 'Azul', 'Verde']
random_color = random.choice(colors)
print(random_color)

#barajar una lista de cartas
cards = ['As', 'rey', 'reina', 'J', '10']
random.shuffle(cards)
print(cards)