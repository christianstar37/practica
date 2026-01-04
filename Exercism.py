def capitalize_title(title):    
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """
    
    title_first_upper = ''
    palabras = title.split()
    for palabra in palabras:
        title_first_upper += palabra[0].upper() + palabra[1:] + ' '
    return title_first_upper.strip()

def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """
    
    return sentence.strip(' ')

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

def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """
    
    return sentence.strip(' ')

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    if ticket_type == 0: 
        normal_queue.append(person_name) 
        return normal_queue
    else: 
        express_queue.append(person_name)
        return express_queue

def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    student_scores_rounds = []
    while student_scores:
        score = student_scores.pop(0)
        if type(score) == float:
            score = round(score)
        student_scores_rounds.append(score) 
    return student_scores_rounds

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    return [41, round(highest*0.56), round(highest*0.71), round(highest*0.86)]

def steps(number):
    if isinstance(number, int) and number > 0:
        step = 0
        while number != 1:
            if number % 2 == 0:
                number //= 2
            else:
                number *= 3
                number += 1
            step += 1
        return step
    else:
        raise ValueError('Only positive integers are allowed')

def is_armstrong_number(number):
    armstrong = 0
    for num in str(number):
        armstrong += (int(num) ** len(str(number))) 
    return armstrong == number

def convert(number):
    sound = ''
    if number % 3 == 0: sound += 'Pling'
    if number % 5 == 0: sound += 'Plang'
    if number % 7 == 0: sound += 'Plong'
    if sound == '': sound = number
    return sound

def translate(text):
    words = text.split()
    count = len(text.split())
    text_out = ''
    while count != 0:
        word = list(words[-count])
        rule_1 = ('a', 'e', 'i', 'o', 'u', 'xr', 'yt')
        rule_3_count = text.find('qu')
        rule_4_count = text.find('y')
        if text.startswith(rule_1): pass
        elif 'q' in word and 'u' in word and rule_3_count <= 1: 
            while word[-1] != 'u':
                word.extend(word.pop(0))
        elif 'y' in word and rule_4_count <= 2 and rule_4_count != 0:
            while word[0] != 'y':
                word.extend(word.pop(0))
        else: 
            while not word[0] in rule_1:
                word.extend(word.pop(0))
        text_out += ''.join(word) + 'ay '
        count -= 1
    return text_out.strip()

def is_paired(input_string): # primer intento de este código, en los siguientes se soluciona los problemas
    start_1 = input_string.find('{')
    end_1 = input_string.find('}')
    start_2 = input_string.find('[')
    end_2 = input_string.find(']')
    start_3 = input_string.find('(')
    end_3 = input_string.find(')')

    start_list = [start_1, start_2, start_3]
    end_list = [end_1, end_2, end_3]

    if '{' in input_string and '}' in input_string and start_1 < end_1 and input_string.count('{') == input_string.count('}'): cond_1 = True
    elif '{' in input_string or '}' in input_string: cond_1 = False
    else: cond_1 = True

    if '[' in input_string and ']' in input_string and start_2 < end_2 and input_string.count('[') == input_string.count(']'): cond_2 = True
    elif '[' in input_string or ']' in input_string: cond_2 = False
    else: cond_2 = True

    if '(' in input_string and ')' in input_string and start_3 < end_3 and input_string.count('(') == input_string.count(')'): cond_3 = True
    elif '(' in input_string or ')' in input_string: cond_3 = False
    else: cond_3 = True

    return cond_1 and cond_2 and cond_3

def is_paired(input_string): # el siguiente código lo he acabado sacando en parte con la IA porque no me daba la cabeza
    inicio = '([{'
    final = ')]}'
    memoria = []

    for character in input_string:
        if character in inicio:
            memoria.append(character)
        elif character in final:
            if not memoria:
                return False

            posicion = final.index(character)
            ultimo = memoria.pop()

            if ultimo != inicio[posicion]:
                return False

    return len(memoria) == 0

def is_paired(input_string): # este código es igual que el anterior pero explicado línea a línea para poder entederlo
    memoria = [] # Aquí se introducirán los caracteres de entrada y se comprobarán su posición
    inicio = '([{' # caracteres de entrada
    fin = ')]}' # caracteres de salida
    for character in input_string: # comprobamos cada caracter que haya en nuestro input
        if character in inicio: # si es uno de entrada
            memoria.extend(character) # lo introducimos en la lista de memoria
        elif character in fin: # en caso de ser uno de salida
            if not memoria: # y que no haya nada en memoria
                return False # se retornará un False debido a que si hay un caracter de salida debe haberse introducido uno de entrada primero
            
            posicion = fin.index(character) # tomamos la posición que tiene el caracter de salida en la string fin
            ultimo = memoria.pop() # tomamos el último valor que se introdujo en memoria
            
            if ultimo != inicio[posicion]: # comprobamos que la posición del caracter de salida que tenemos coincida con el la posición del último de entrada que se introdujo
                return False # en caso de que no coincida se retornará False ya que el orden estaría mal
            
    return len(memoria) == 0 # como todos los caracteres de entrada en memoria se han tenido que sacar al tener un cierre la longitud de la lista debe ser 0, es decir, True

def is_isogram(string): # este código se puede acortar muchísimo con el uso de set {}
    memory = []
    string = string.lower()
    for character in string:
        if not character in memory and character.isalpha():
            memory.extend(character)
        elif character in memory:
            return False
    return True

def rotate(text, key):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = plain[key:] + plain[:key]
    text_rot = ''
    for char in text:
        if char.lower() not in cipher:
            text_rot += char
        elif char.islower():
            position = plain.find(char)
            text_rot += cipher[position]
        elif char.isupper():
            position = plain.find(char.lower())
            text_rot += cipher[position].upper()
    return text_rot

def array_diff(a, b):
    for number in a[:]:
        if number in b: a.remove(number)
    return a

