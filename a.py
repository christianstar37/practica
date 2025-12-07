import random

nombres = ["Ana", "Luis", "Carlos", "María", "Elena", "Pedro", "Lucía", "Javier"]
random.shuffle(nombres)

def waifus_husbandos(lista, tamaño):
    """Devuelve una tanda y elimina esos nombres de la lista."""
    tanda = lista[:tamaño]
    del lista[:tamaño]
    return tanda

ronda = 0

input("Pulsa ENTER para empezar ")

# Ejemplo de uso
while nombres:
    print("")
    elegidos = waifus_husbandos(nombres, 3)
    ronda += 1
    print(str(ronda) + "º Ronda:", elegidos)
    print("")
    input("Pulsa ENTER para pasar a la siguiente ronda...")

print("Ya no quedan papelitos.")