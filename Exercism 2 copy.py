prueba = 'prueba de mayúsculas por cada letra'
prueba_2 = 'hoy en clase nos han cambiado de sitio'


"""Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """
def capitalize_title(title):    
    title_first_upper = ''
    palabras = title.split()
    for palabra in palabras:
        title_first_upper += palabra[0].upper() + palabra[1:] + ' '
    return title_first_upper.strip()

print(capitalize_title(prueba))
print(capitalize_title(prueba_2))

def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """
    
    return sentence.strip(' ')

print(clean_up_spacing(prueba))
print(clean_up_spacing(prueba_2))

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.    
    if card_one == 'J' or 'Q' or 'K': card1_val = 10
    elif 'A': card1_val = 11
    else: card1_val = card_one
    
    if card_two == 'J' or 'Q' or 'K': card2_val = 10
    elif 'A': card2_val = 11
    else: card2_val = card_one
    
    if card_one == 'A' or card_two == 'A': return 1
    else: return 11
    
    """
    if card_one in ['J', 'Q', 'K']: card1_val = 10
    elif card_one == 'A': card1_val = 11
    else: card1_val = int(card_one)
    
    if card_two in ['J', 'Q', 'K']: card2_val = 10
    elif card_two == 'A': card2_val = 11
    else: card2_val = int(card_two)
    
    if card1_val + card2_val + 11 <= 21: return 11 
    else: return 1
    
    
    
print(value_of_ace('2','3'))
print(value_of_ace('K','K'))
print(value_of_ace('1','1'))
print(value_of_ace('3','3'))