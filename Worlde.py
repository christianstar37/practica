# Wordle en Python

import random

# bolsita de palabras, again
palabras = ["CASAS","PERRO","GATOS","ARBOL","SOLAR","LIMON","NIEVE","LETRA","FORMA","LIBRO",
            "PLANO","SILLA","CIELO","MARCO","MUNDO","FRUTA","PASTA","CAMPO","RATON","LLAVE"]


# palabra que hay que adivinar
palabra_real = random.choice(palabras)
palabra_real = 'CASAS'
palabra_int = input('¿Con qué palabra quieres probar?\n')
print('')
palabra_temp = '_____'

# función para compronar si la palabra dicha tiene alguna coincidencia con la real
def intento(palabra_int, palabra_temp):

    # bucle de comprobación
    for pos_t, let_t in enumerate(palabra_real):
        for pos_p, let_p in enumerate(palabra_int.upper()):
            if let_p == let_t and pos_p == pos_t:
                palabra_temp = palabra_temp[:pos_p] + let_p + palabra_temp[pos_p+1:]
            elif let_p == let_t and pos_p != pos_t:
                print(f'La letra {let_p} está en otra posición')
    return palabra_temp

palabra_temp = intento(palabra_int, palabra_temp)

print(palabra_temp)

# bucle para probar las palabras hasta llegar a la real
while palabra_real != palabra_temp:
    palabra_int = input('\n¿Con qué palabra quieres probar?\n')
    palabra_temp = intento(palabra_int, palabra_temp)
    print(palabra_temp)

# mensaje final
print('\nEnhorabuena, la palabra era',intento(palabra_int, palabra_temp))
input('')