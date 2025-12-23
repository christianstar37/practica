#Trabajo informática

print("Bienvenidos al Pyzoo.")
Animales = ["Lobo", "Zorro", "Panda", "Jirafa", "Cocodrilo", "Guepardo", "Flamenco",
            "Pingüino", "Tortuga", "Elefante", "Leon", "Gorila", "Loro", "Águila",
            "Delfin"]

Carnivoros = ["Lobo", "Cocodrilo", "Guepardo", "Pingüino", "Leon", "Aguila", "Delfin"]
Herbivoros = ["Panda", "Jirafa", "Elefante", "Loro"]
Omnivoros = ["Zorro", "Flamenco", "Tortuga", "Gorila"]

Montaña = ["Lobo", "Flamenco", "Aguila"]
Sabana = ["Jirafa", "Cocodrilo", "Guepardo", "Elefante", "Leon"]
Mar = ["Tortuga", "Delfin"]
Artico = ["Pingüino"]
Bosque = ["Lobo", "Zorro", "Panda"]
Selva = ["Gorila", "Loro"]

Mamiferos = ["Lobo", "Panda", "Zorro", "Jirafa", "Guepardo", "Elefante", "Leon", "Gorila", "Delfin"]
Reptiles = ["Cocodrilo", "Tortuga"]
Aves = ["Flamenco", "Pingüino", "Loro", "Aguila"]

Cantidad = {"Lobo": 15, "Zorro": 10, "Panda":8, "Jirafa": 12, "Cocodrilo": 14, "Guepardo": 10,
            "Flamenco": 20, "Pingüino": 16, "Tortuga": 23, "Elefante": 8, "Leon":14, "Gorila": 7,
            "Loro": 12, "Águila": 10, "Delfin": 4}

Ubicacion={"Acuario" : ["Tortuga", "Delfin", "Pingüino"],
           "Jaulas" : ["Aguila"],
           "Seccion3" : ["Lobo", "Zorro"],
           "Seccion4" : ["Flamenco"],
           "Seccion5" : ["Jirafa", "Guepardo", "Elefante", "Leon", "Cocodrilo", "Gorila"],
           "Seccion6" : ["Panda"]}

Curiosidades = {"Lobo":"Una pareja de lobos permanece unida para siempre, si uno muere, el otro también", 
              "Panda":"A pesar de ser una clase de osos, no hibernan",
              "Zorro":"Se guían por el campo magnético de la Tierra",
              "Jirafa":"Su lengua puede llegar a medir 50 centimetros y es azul",
              "Cocodrilo":"Pueden vivir hasta 80 años",
              "Guepardo":"Corre hasta una velocidad de hasta 113 km/h",
              "Flamenco":"Duermen de pie",
              "Pingüino":"Pueden dar saltos de hasta 2 metros de altura",
              "Tortuga":"Fue el primer animal en viajar a la luna y regresar en 1968",
              "Elefante":"Se refrescan moviendo las orejas",
              "Leon":"Durante la época reproductiva pueden copular más de 3000 veces",
              "Gorila":"Pueden llorar pero no sueltan lágrimas, solo hacen ruido",
              "Loro":"Son monóganos de por vida",
              "Aguila":"Empolla dos huevos pero el más grande mata al más pequeño",
              "Delfin":"Duermen con un ojo abierto"}

accion = input("¿Que acción desea realizar?¿Consulta, añadir, eliminar, ver mapa o salir?: ")
salir = 0
while salir != 1:
    if accion == "salir":
        salir = 1
    elif accion == "consulta":
        consultar2 = ["Animales", "Alimentacion", "Habitat", "Clasificacion",
                      "Cantidad", "Ubicacion en el zoo", "Curiosidades"]
        
        consultar= str(input("¿Que información desea consultar{}: ".format(consultar2)))
        if consultar == "Animales" or "animales":
            print(Animales)
        elif consultar == "Alimentación" or "alimentacion":
            alim=input("¿Qué tipo de alimentación desea consultar? \n a)Carnívoro \n b)Hervíboro \n c)Omnívoro \n") 
            if alim == "a" or "carnivoro":
                print (Carnivoros)
            elif alim == "b" or "herbivoro":
                print (Herbivoros)
            elif alim == "c" or "omnivoro":
                print (Omnivoros) 
        elif consultar == "Habitat" or "habitat":
            habit = input("¿Qué tipo de origen desea consultar? \n a)Bosque \n b)Montaña \n c)Sabana \n d)Mar \n e)Ártico \n f)Selva \n") 
            if habit == "a" or "bosque":
                print (Bosque)
            elif habit == "b" or "montaña":
                print (Montaña)
            elif habit == "c" or "sabana":
                print (Sabana)
            elif habit == "d" or "mar" :
                print (Mar)
            elif habit == "e" or "artico":
                print (Artico)
            elif habit == "f" or "selva":
                print (Selva)
                
        elif consultar == "Clasificacion" or "clasificacion":
            clas = input("¿De qué clase de animales desea ver un listado, \nMamíferos, reptiles o aves? \n")
            if clas == "Mamiferos" or "mamiferos":
                print(Mamiferos)
            elif clas == "Reptiles" or "reptiles":
                print(Reptiles)
            elif clas == "Aves" or "aves":
                print(Aves)
                
        elif consultar == "Cantidad" or "cantidad":
            print(Cantidad.items())
            
        elif consultar == "Ubicación" or "ubicacion":
            print(Ubicacion.items())
            
        elif consultar == "Curiosidades" or "curiosidades":
            print (Curiosidades.items())
            
        else:
            print("Esa opción no está disponible, por favor inténtelo de nuevo")
    elif accion == "añadir":
        repe = int(input("¿Cuántos animales desea añadir?: "))
        for k in range (0, repe):
            nombre = input ("Indique el nombre del animal: ")
            Animales.append(nombre)
            
            alimentacion = input("Indique si es carnívoro, herbívoro u omnívoro: ")
            if alimentacion == "carnivoro":
                Carnivoros.append(nombre)
            elif alimentacion == "herbivoro":
                Herbivoros.append(nombre)
            elif alimentacion == "omnivoro":
                Omnivoros.append(nombre)       
                
            habitat = input("Indique el habitat de este animal: (Selva, bosque, montaña, sabana, mar o ártico: \n")
            if habitat == "Selva" or "selva":
                Selva.append(nombre)
            elif habitat == "Bosque" or "bosque":
                Bosque.append(nombre)
            elif habitat == "Montaña" or "montaña":
                Montaña.append(nombre)
            elif habitat == "Sabana" or "sabana":
                Sabana.append(nombre)
            elif habitat == "Mar" or "mar":
                Mar.append(nombre)
            elif habitat == "Ártico" or "Artico" or "ártico" or "artico":
                Artico.append(nombre)
                
            clasif = input("¿Qué clase de animal es?")
            if clasif == "Mamífero" or "mamifero":
                Mamiferos.append(nombre)
            elif clasif == "Reptil" or "reptil":
                Reptiles.append(nombre)
            elif clasif == "Ave" or "ave":
                Aves.append(nombre)
                
            cant = int(input("¿Cuántos individuos de este animal vamos a añadir al zoo?"))
            Cantidad[nombre] = cant

            ubica = input("¿En qué zona del zoo se intrudicirá a este animal?.format{}".format(Ubicacion.keys()))
            Ubicacion[ubica].append(nombre)
            
            curios = input("Indique una curiosidad sobre el animal: ")
            Curiosidades[nombre] = curios
            
    elif accion == "eliminar":
        print(Animales)
        repe2 = int(input("¿Cuántos animales desea eliminar?: "))
        for k in range (0, repe2):
            nombre2 = input("Indique el nombre del animal que desea eliminar (se eliminará junto a todos sus datos): ")
            Animales.remove(nombre2)
            if nombre2 in Carnivoros:
                Carnivoros.remove(nombre2)
            elif nombre2 in Herbivoros:
                Herbivoros.remove(nombre2)
            elif nombre2 in Omnivoros:
                Omnivoros.remove(nombre2)
                
            if nombre2 in Montaña:
                Montaña.remove(nombre2)
            elif nombre2 in Sabana:
                Sabana.remove(nombre2)
            elif nombre2 in Mar:
                Mar.remove(nombre2)
            elif nombre2 in Artico:
                Artico.remove(nombre2)
            elif nombre2 in Bosque:
                Bosque.remove(nombre2)
            elif nombre2 in Selva:
                Selva.remove(nombre2)
                    
            if nombre2 in Mamiferos:
                Mamiferos.remove(nombre2)
            elif nombre2 in Aves:
                Aves.remove(nombre2)
            elif nombre2 in Reptiles:
                Reptiles.remove(nombre2)
                
            if nombre2 in Cantidad:
                del Cantidad[nombre2]
                
            if nombre2 in Ubicacion:
                del Ubicacion[nombre2]
                
            if nombre2 in Curiosidades:
                del Curiosidades[nombre2]
                

    else:
        print("Te has equivocado, inténtalo de nuevo")
        