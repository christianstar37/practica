def contador():

    texto = input('Introduce un texto: ')
    palabras = texto.split()

    if len(palabras) > 1: print(len(palabras), 'palabras.')
    else: print('Texto no válido')
    return

contador()