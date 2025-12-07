import pandas as pd

ghosts =  {
    "Nombre": ['Hetty', 'Isaac', 'Alberta', 'Pete', 'Sassappis', 'Flower', 'Trevor', 'Thorfinn', 'Patience', 'Stephanie'],
    "Edad": [45, 35, 38, 41, 25, 31, 33, 38, 40, 18],
    "Año de muerte": [1895, 1777, 1928, 1985, 1513, 1969, 2000, 1007, 1692, 1987],
    "Poder": ["San Patricio", "Olor", "Cantar", "Sin límite", "Sueños", "Porros", "Tocar cosas", "Rayos", "Jesucristo", "No tiene"],
    "Relación": ["Por supuesto", "No", "Sí", "Sí", "Sí", "Sí", "Por supuesto", "Sí", "No", "No"]
}

ghosts = pd.DataFrame(ghosts)

ghosts["Causa de muerte"] = ["Estrangulación", "Disentería", "Envenenada", "Flecha", "Desconocida", "Ataque de oso", "Sobredosis", "Electrocutado", "Flebotomía", "Asesino en serie"]

ghosts_edad = ghosts.sort_values(by="Edad", ascending=False)

ghosts_poderes = ghosts[["Nombre","Poder"]]

ghosts_mayores = ghosts[ghosts["Edad"] > 35]