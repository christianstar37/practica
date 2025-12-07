print("Ha costado, pero creo que he hecho un sombrero seleccionador.")

entendido = input("Responde sólo con números, nada de texto. Entendido? (Aquí sí puedes escribir lo que quieras) ")

g = 0
s = 0
h = 0
r = 0

print("Q1. ¿Qué prefieres, el amanecer o el atardecer?")
print("1) Amanecer.")
print("2) Atardecer.")
Q1 = int(input(""))

if Q1 == 1:
    g = g + 1
    r = r + 1
elif Q1 == 2:
    h = h + 1
    s = s + 1
else:
    print("Input incorrecto")

print("Q2. Cuando esté muerto quiero que la gente me recuerde como...")
print("1) El bueno.")
print("2) El mejor.")
print("3) El sabio.")
print("4) El gracioso.")
Q2 = int(input(""))

if Q2 == 1:
    h = h + 2
elif Q2 == 2:
    s = s + 2
elif Q2 == 3:
    r = r + 2
elif Q2 == 4:
    g = g + 2
else:
    print("Input incorrecto")
    
print("Q3. ¿Qué instrumento te gusta más escuchar?")
print("1) El violín.")
print("2) La trompeta.")
print("3) El piano.")
print("4) El tambor.")
Q3 = int(input(""))

if Q3 == 1:
    s = s + 4
elif Q3 == 2:
    h = h + 4
elif Q3 == 3:
    r = r + 4
elif Q3 == 4:
    g = g + 4
else:
    print("Input incorrecto")

if g > s and g > r and g > h:
    print("Tu casa es Griffindor!")
elif s > g and s > r and s > h:
    print("Tu casa es Slytherin!")
elif r > g and r > s and r > h:
    print("Tu casa es Ravenclaw!")
else:
    print("Tu casa es Hufflepuff!")