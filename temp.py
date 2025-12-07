import random

print('')
input('Os vas a hinchar a pulsar ENTER cada vez que veas una línea como esta... preparados? (Pulsa ENTER)')
input('¿Qué sería de una pijamada de las nuestras sin un buen... BESAR, CASAR Y MATAR?')
input('Me he hinchado pero he hecho unas cuantas "bolsitas" de nuestros típicos papelitos.')
def elegir_fandom():
    input('Aquí podéis elegir con que fandom queéis jugar. Lo que vereís entre paréntesis es el número de personajes que tiene cada uno, debería ser multiplo de 3... En caso de no serlo echadle la culpa al Christian del pasado, no al majo ese que tenéis al lado.')

    print("")
    print('+-------------------------------------------+')
    print('+--  1. Helluva Boss  -------------------(21)')
    print('+--  2. Hazbin Hotel  -------------------(27)')
    print('+--  3. Helluvaverse  -------------------(48)')
    print('+--  4. The Owl House  ------------------(30)')
    print('+--  5. Animación  ----------------------(78)')
    print('+-------------------------------------------+')
    print('+--  6. One Piece  ----------------------(87)')
    print('+--  7. Naruto  -------------------------(54)')
    print('+--  8. Otros animes  ------------------(102)')
    print('+--  9. Animes  ------------------------(243)')
    print('+-------------------------------------------+')
    print('+--  10. Libros  ------------------------(24)')
    print('+-------------------------------------------+')
    print('+--  11. El MEGA MIX (Todos)  ----------(345)')
    print('+-------------------------------------------+')
    print('')
    conjunto = int(input('Escribe el número de la bolsita que os interesa (He puesto "os" así que decidid democráticamente): '))
    secreto = 0

    Helluva_Boss = ['Blitzø', 'Luna', 'Moxxie', 'Millie', 'Asmodeus', 'Queen Bee', 'Mammon', 'Satan', 'Stolas', 'Octavia', 'Stella', 'Andrealphus', 'Vassago', 'Verosika', 'Vortex', 'Fizzarolli', 'Striker', 'Chazwick', 'Amberlynn', 'Crimson', 'Leviathan']
    Hazbin_Hotel = ['Charlie', 'KeeKee', 'Lucifer', 'Lilith', 'Vaggie', 'Adam', 'Lute', 'Angel Dust', 'Husk', 'Alastor', 'Niffty', 'Sir Pentious', 'Razzle', 'Dazzle', 'Cherri Bomb', 'Huevitos (los 5)', 'Sera', 'Emily', 'San Pedro', 'Fat Nuggets', 'Rosie', 'Vox', 'Velvette', 'Valentino', 'Carmila', 'Zestial', 'Katie (Presentadora)']
    The_Owl_House = ['Luz Noceda', 'Eda Clawthorne', 'King Clawthorne', 'Hooty', 'Amity Blight', 'Willow', 'Gus', 'Lilith Clawthorne', 'Belos', 'Hunter', 'Kikimora', 'Owlbert', 'Director Bump', 'Emira Blight', 'Edric Blight', 'Boscha', 'Alador Blight', 'Odalia Blight', 'El Coleccionista', 'Tinella Nose', 'Darius Deamonne', 'Fantasma', 'Flapjack', 'Stringbean', 'Bat Queen', 'Raine Whispers', 'Camila Noceda', 'Vee', 'Gwendolyn Clawthorne', 'Terra Dragonaria']
    One_Piece = ['Luffy', 'Zoro', 'Nami', 'Usopp', 'Sanji', 'Chopper', 'Robin', 'Franky', 'Brook', 'Jinbe', 'Ace', 'Sabo', 'Law', 'Boa', 'Carrot', 'Yamato', 'Shanks', 'Corazon', 'Katakuri', 'Crocodile', 'Marco', 'Doflamingo', 'Vivi', 'Bon Clay', 'Kid', 'Perona', 'Oden', 'Smoker', 'Roger', 'Mihawk', 'Shirohige', 'Rayleigh', 'Buggy', 'Enel', 'Aokiji', 'Tashigi', 'Bartolomeo', 'X Drake', 'Coby', 'Lucci', 'La paloma del Infierno', 'Niji', 'Ichiji', 'Reiju', 'Yonji', 'Garp', 'Pudding', 'Kurohige', 'Smothie', 'Shirahoshi', 'Hiyori', 'O-Kiku', 'Fujtora', 'Akainu', 'Kaku', 'Bepo', 'Benn Beckman', 'Koala', 'Kizaru', 'Pedro', 'Nekomamushi', 'Inuarashi', 'Wanda', 'Dragon', 'Kaido', 'Big Mom', 'Rebecca', 'Sr. Pink', 'Cavendish', 'Moria', 'Monet', 'Ivankov', 'Ulti', "Kin'emon", 'Bonny', 'Cracker', 'Kuma', 'Perospero', 'Zeff', 'Sora', 'Judge', 'Kushina', 'Arlong', 'Black Maria', 'Saint Charlos', 'Spandam', 'Brulée']

    Naruto = ['Naruto', 'Sakura', 'Sasuke', 'Kakashi', 'Kurama', 'Jiraiya', 'Tsunade', 'Orochimaru', 'Hinata', 'Neji', 'Ino', 'Shikamaru', 'Choji', 'Asuma', 'Kurenai', 'Temari', 'Kanjuro', 'Gaara', 'Shino', 'Karin', 'Minato', 'Kushina', 'Madara', 'Hashirama', 'Madara', 'Tobirama', 'A', 'Tsuchikage', 'Mei', 'Killer Bee', 'Obito', 'Nagato', 'Kabuto', 'Sasori', 'Kisame', 'Hidan', 'Deidara', 'El Cuervo de Itachi', 'Itachi', 'Shisui', 'Rock Lee', 'Might Guy', 'Iruka', 'Ichiraku', 'Zabuza', 'Haku', 'Konan', 'Sai', 'Yamato', 'Kiba', 'Akamaru', 'Shizune', 'Dan', 'Rin']

    Assasination_Classroom = ['Koro-sensei', 'Nagisa', 'Karma', 'Bitch-sensei', 'Karasuma']
    Black_Clover = ['Asta', 'Yuno', 'Noelle', 'Zora', 'Mimosa', 'Henry', 'Licita', 'Fuegoleon', 'Mereoleona', 'Yami', 'Vanica', 'Charlotte', 'Nero', 'Julius', 'Natch', 'Vanessa', 'Dante', 'Nozel', 'Loropechika']
    Bleach = ['Ichigo', 'Rukia', 'Renji', 'Orihime', 'Ishida', 'Chad', 'Ikkaku', 'Zangetsu', 'Shunsui', 'Unohana', 'Kenpachi', 'Komamura', 'Arisawa', 'Kensei', 'Yoruichi', 'Urahara', 'Grimmjow', 'Rangiku', 'Ulquiorra', 'Byakuya', 'Shinji', 'Nanao', 'Yhwach', 'Neliel', 'Mayuri', 'Nemu', 'Jefa Ichigo', 'Aizen']
    Jujutsu_Kaisen = ['Itadori', 'Nobara', 'Megumi', 'Gojou', 'Nanami', 'Sukuna', 'Panda', 'Inumaki', 'Maki', 'Todo']
    My_Hero_Academia = ['Deku', 'Bakugo', 'Todoroki', 'Uraraka', 'Denki', 'Midnight', 'Denki', 'All Might', 'All for One', 'Recovery Girl', 'Mineta', 'Himiko Toga', 'Hawks', 'Poli BNHA', 'Nejire', 'Mt. Lady', 'Gang Orca', 'Twice', 'Dabi', 'Kirishima', 'Fat Gum', 'Shinso', 'Eri','Aizawa', 'Shigaraki', 'Muscular', 'Lady Nagant', 'Mirio']
    Danganronpa = ['Monokuma', 'Makoto Naegi', 'Aoi Asahina', 'Byakuya Togami', 'Chihiro Fujisaki', 'Leon Kuwata', 'Enoshima Junko', 'Kyoko Kirigiri', 'Sakura Ogami', 'Celestia Ludenberg', 'Toko Fukawa', 'Monomi']

    Libros = ['Nesta', 'Cassian', 'Feyre', 'Rhysand', 'Mor', 'Amren', 'Tamlin', 'Elaine', 'Lucian', 'Azriel', 'Gwyn', 'El Suriel', 'Emerie', 'Rowan', 'Aelin', 'Manon', 'Chaol', 'Dorian', 'Aedion', 'Missy', 'Lowe', 'Serena', 'Hoid', 'Eris']
    Cosmere = ['Kaladin', 'Syl', 'Shallan', 'Patrón', 'Dalinar Kholin', 'Navani Kholin', 'Adolin Kholin', 'Renarin Kholin', 'Roca', 'Teft', 'El Lopen', 'Vin', 'Sadeas', 'Moash', 'Amaram', 'Taravangian', 'Cikatriz', 'Lift', 'Padre Tormenta', 'El Hermano', 'Hesina', 'Palona', 'Lirin' , 'Sebarial', 'Jasnah', 'Szeth' , 'Maya']

    #página para ver las fotos de los de Danganronpa: https://danganronpa.fandom.com/wiki/Anime_Characters#Danganronpa_1

    Danganronpa2 = ['Monokuma', 'Makoto Naegi', 'Aoi Asahina', 'Byakuya Togami', 'Chihiro Fujisaki', 'Leon Kuwata', 'Enoshima Junko', 'Kyoko Kirigiri', 'Sakura Ogami', 'Celestia Ludenberg', 'Toko Fukawa', 'Monomi', 'Chisa Yukizome', 'Juzo Sakakura', 'Kyosuke Munakata', 'Ruruka Ando', 'Seiko Kimura', 'Sonosuke Izayoi', 'Hajime Hinata', 'Chiaki Nanami', 'Akane Owari', 'Ibuko Mioda', 'Kazuichi Soda', 'Nagito Komaeda', 'Peko Pekoyama', 'Sonia Nevermind', 'Mikan Tsumiki', 'Mahiru Koizumi', 'Gundham Tanaka', 'Fuyuhiko Kuzuryu', 'Hoyoko Saionji']

    Clásicos = Assasination_Classroom + Black_Clover + Bleach + Jujutsu_Kaisen + My_Hero_Academia + Danganronpa


    if conjunto == 1:
        fandom = Helluva_Boss
        bolsita = 'Helluva'
    elif conjunto == 2:
        fandom = Hazbin_Hotel
        bolsita = 'Aitor empiézate la segunda'
    elif conjunto == 3:
        fandom = Helluva_Boss + Hazbin_Hotel
        bolsita = 'El Helluvaverso'
    elif conjunto == 4:
        fandom = The_Owl_House
        bolsita = 'La casa Hooty'
    elif conjunto == 5:
        fandom = Helluva_Boss + Hazbin_Hotel + The_Owl_House
        bolsita = 'Sí, sabía que querríais esto'
    elif conjunto == 6:
        fandom = One_Piece
        bolsita = 'Una pieza'
    elif conjunto == 7:
        fandom = Naruto
        bolsita = 'Naruto: Boruto Previous Generation'
    elif conjunto == 8:
        fandom = Clásicos
        bolsita = 'Un poquito de mix animes'
    elif conjunto == 9:
        fandom = One_Piece + Naruto + Clásicos
        bolsita = 'Se dijo sí al anime'
    elif conjunto == 11:
        fandom = Helluva_Boss + Hazbin_Hotel + The_Owl_House + One_Piece + Naruto + Clásicos + Libros
        bolsita = 'Sois conscientes de que son huevo y nos vamos a pasar con esto toda la noche?' 
    elif conjunto == 10:
        fandom = Libros
        bolsita = 'Algunos personajes de libritos'
    elif conjunto == 12:

        print('')
        input('Holi, acabas de entrar en el modo secreto, esto es un modo súper secreto. Tan secreto que no está ni desarrollado. No me daba la vida para hacer alguna cosa chula como la que me gustaría aquí. Pero... quizás la próxima vez?')
        secreto = input('Bueno venga, un poquito secreto sí que va a ser. ')
        bolsita = 'Secretos'
        print("")
        print('+-----------------------------------------+')
        print('+--  1. Assasination Classroom  ----------+')
        print('+--  2. Black Clover  --------------------+')
        print('+--  3. Bleach  --------------------------+')
        print('+--  4. Jujustus Kaisen  -----------------+')
        print('+--  5. Boku no Hero Academia  -----------+')
        print('+--  6. Danganronpa  ---------------------+')
        print('+--  7. Cosmere  -------------------------+')
        print('+-----------------------------------------+')
        print('')

        secreto = int(input('Elegís el '))
    else: 
        pass

    print('')

    seguro = input('Habéis elegido la bolsita: ' + bolsita + '. Estáis seguros? [Y/N] ').upper()

    if secreto == 0:
        pass
    elif secreto == 1:
        fandom = Assasination_Classroom
    elif secreto == 2:
        fandom = Black_Clover
    elif secreto == 3:
        fandom = Bleach
    elif secreto == 4:
        fandom = Jujutsu_Kaisen
    elif secreto == 5:
        fandom = My_Hero_Academia
    elif secreto == 6:
        fandom = Danganronpa2
        print('')
        print('Por si queréis ir a ver a los personajes: https://danganronpa.fandom.com/wiki/Anime_Characters#Danganronpa_1')
    elif secreto == 7:
        fandom = Cosmere
    else: 
        fandom = 0

    return fandom

def waifus_husbandos(lista, tamaño):
    """Devuelve una tanda y elimina esos nombres de la lista."""
    tanda = lista[:tamaño]
    del lista[:tamaño]
    return tanda

seguir = 'Y'

while seguir == 'Y':
    ronda = 0
    
    nombres = elegir_fandom()
    random.shuffle(nombres)

    print('')

    input("Pulsa ENTER para empezar ")

    # Esto es lo que genera las rondas
    while nombres:
        print('')
        elegidos = waifus_husbandos(nombres, 3)
        ronda += 1
        print(str(ronda) + "º ronda:", ' | '.join(elegidos))
        print("")
        print("")
        print("")
        input("Pulsa ENTER para pasar a la siguiente ronda")

    print('')
    input("Ya no quedan papelitos en la bolsita.")
    print('')
    seguir = input('Queréis otra? [Y/N] ').upper()
    print('')
