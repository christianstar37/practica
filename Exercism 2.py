prueba = ' Prueba de mayúsculas por cada letra. '
prueba_2 = ' Hoy en clase nos han cambiado de sitio. '

def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """
    
    return sentence.strip(' ')

print(clean_up_spacing(prueba))
print(clean_up_spacing(prueba_2))