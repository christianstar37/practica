prueba = 'prueba de mayúsculas por cada letra'
prueba_2 = 'hoy en clase nos han cambiado de sitio'

def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """

    palabras = title.split()
    primera_mayus = ''
    for palabra in palabras:
        for i, char in enumerate(palabra):
            if i == 0:
                primera_mayus += char.upper()
            else:
                primera_mayus += char
        primera_mayus += ' '
    return primera_mayus.strip()

print(capitalize_title(prueba))
print(capitalize_title(prueba_2))