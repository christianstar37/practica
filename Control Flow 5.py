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