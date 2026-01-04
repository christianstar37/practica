def star_rating():

    print("")
    rating = float(input("Star number? "))
    print("")
    print("===========================")
    print("")
    if rating > 4.5:
        print("Extraordinary!")
    elif rating > 4:
        print("Excellent!")
    elif rating > 3:
        print("Good!")
    elif rating > 2:
        print("Fair")
    else:
        print("Poor")
    print("")
    return

def school_grade():

    grade = int(input("Grade? "))

    if grade == 9:
        print("Freshman")
    elif grade == 10:
        print("Sophomore")
    elif grade == 11:
        print("Junior")
    elif grade == 12:
        print("Senior")
    else:
        print("TBD")
        return


def fun_fact():

    import random

    snapple = random.randint(0,5)

    print("")
    print("======================================================")
    print("                       FUN FACT                       ")
    print("======================================================")

    if snapple == 0:
        print("Flamindos turn pink from eating shrimp.")
    elif snapple == 1:
        print("The only food that doesn't spoil is honey.")
    elif snapple == 2:
        print("Shrimp can only swim backyards.")
    elif snapple == 3:
        print("A taste bud's life span is about 10 days.")
    elif snapple == 4:
        print("It is impossible to sneeze while sleeping")
    else:
        print("It is illegal to sing off-key in North Carolina")

    print("======================================================")
    print("")
    return


def actual_season():

    n_month = int(input("What is the number of the current month? "))

    if n_month <= 3:
        print("Winter!")
    elif n_month <= 6:
        print("Spring!") 
    elif n_month <= 9:
        print("Summer!")
    elif n_month <= 12:
        print("Autumn!")  
    else:
        print("Invalid")
    return


def gravedad_planetaria():

    print("")
    print("Como sabrás en cada planeta tienes un peso distinto debido a la gravedad de cada uno, vamos a ver cuál es tu peso en otro planeta!")
    print("")
    print("Aquí te dejo los planetas y sus números:")
    print("")
    print("1: Mercurio")
    print("2: Venus")
    print("3: Marte")
    print("4: Jupiter")
    print("5: Saturno")
    print("6: Urano")
    print("7: Neptuno")
    print("")

    planet = int(input("En cual de estos planetas quieres saber tu nuevo peso? (Inserta un valor numérico) "))
    print("")
    e_weight = float(input("Cuánto pesas en la Tierra? "))

    print("")

    if planet == 1:
        relative = 0.38
        c_planet = "Mercurio"
    elif planet == 2:
        relative = 0.91
        c_planet = "Venus"
    elif planet == 3:
        relative = 0.38
        c_planet = "Marte"
    elif planet == 4:
        relative = 2.53
        c_planet = "Jupiter"
    elif planet == 5:
        relative = 1.07
        c_planet = "Saturno"
    elif planet == 6:
        relative = 0.89
        c_planet = "Urano"
    elif planet == 7:
        relative = 1.14
        c_planet = "Neptuno"
    else:
        print("invalid planet")

    if planet <= 7:
        d_weight = e_weight * relative    
        print("Tu peso en",c_planet,"es de",d_weight,"kg.")
    else:
        pass
    print("")
    return

