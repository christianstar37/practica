# Primer Código (Desfasado)

# novios_a = ['Karasuma']
# novias_a = ['Kurenai']
# novios_irl = ['Oscar Isaac']
# novias_irl = ['Cate Blanchett']
# novias = novias_a + novias_irl
# novios = novios_a + novios_irl
# nov_irl = novias_irl + novios_irl
# nov_a = novias_a + novios_a
# novixs = novias_a + novias_irl + novios_a + novios_irl

# elegidos = novixs

# print('')

# for i in range(len(elegidos))[::-1]:
#     for j in range(len(elegidos)):
#         if i > j:
#             print(f"{elegidos[i]} vs {elegidos[j]}") 

# print('')


# Objetivo:  Crear un bot en discord en el que al poner un ship (Comando corto con las iniciales de los 
#            personajes) me dé una imagen random entre 10 que tenga en una base de datos

# Shipeos para el bot:
#     Gómez & Morticia
#     Christian & Satine
#     Haymitch & Leia
#     Vasher & Vivenna
#     Brisa & Allrianne
#     Dalinar & Navani
#     Wax & Steris
#     Trevor & Hetty

from PIL import Image
import random

choice = int(input('De qué ship quieres la imagen? '))

def img_ship(ship):
    if ship == 1:
        pick = ['1.jpg', '2.jpg', '3.gif']
    random.shuffle(pick)
    return pick[0]

# Gómez_Morticia = ['1.jpg', '2.jpg', '3.gif'] 
# random.shuffle(Gómez_Morticia)

imagen = img_ship(choice)

img = Image.open(imagen)
img.show()