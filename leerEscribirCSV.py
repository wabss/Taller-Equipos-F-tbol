import csv

def calcular_puntos(fila):
    return int(fila["ganados"]) * 3 + int(fila["empatados"])

def diferencia_goles(fila):
    return int(fila["goles_favor"]) - int(fila["goles_contra"]) 

def ordenar(dictEquipos: dict):
    num_equipos = len(dictEquipos)
    nuevo_dict = {}

    def encontrar_mayor():
        clave_mayor = next(iter(dictEquipos))
        valores_mayor = next(iter(dictEquipos.values()))

        for key, value in dictEquipos.items():
            if int(value["puntos"]) > int(valores_mayor["puntos"]):
                clave_mayor = key
                valores_mayor = value

        dictEquipos.pop(clave_mayor)

        return {clave_mayor : valores_mayor}

    while len(nuevo_dict) != num_equipos:
        nuevo_dict.update(encontrar_mayor())

    return nuevo_dict

def liderTabla(dictEquipos):
    clave_mayor = next(iter(dictEquipos))
    valores_mayor = next(iter(dictEquipos.values()))

    for key, value in dictEquipos.items():
        if int(value["puntos"]) > int(valores_mayor["puntos"]):
            clave_mayor = key
            valores_mayor = value
    
    mensaje_final = "Lider de la tabla:" + \
    "\nequipo: " + str(clave_mayor) + \
    "\nganados: " + str(valores_mayor["ganados"]) + \
    "\nperdidos: " + str(valores_mayor["perdidos"]) + \
    "\nempatados: " + str(valores_mayor["empatados"]) + \
    "\npuntos: " + str(valores_mayor["puntos"]) + \
    "\ndiferencia_goles: " + str(valores_mayor["diferencia_goles"])

    return mensaje_final

dictEquipos = {}
with open("equiposChampions.csv", "r") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        dictEquipos[fila["equipo"]] = {
            "ganados": int(fila["ganados"]),
            "empatados": int(fila["empatados"]),
            "perdidos": int(fila["perdidos"]),
            "goles_favor" : int(fila["goles_favor"]),
            "goles_contra" : int(fila["goles_contra"]),
            "puntos" : calcular_puntos(fila),
            "diferencia_goles" : diferencia_goles(fila)
        }

dictEquipos = ordenar(dictEquipos)

with open("equiposSalida.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow(
        ["posicion", "nombre", "ganados", "empatados", "perdidos", "goles_favor", "goles_contra", "puntos", "diferencia_goles"]
    )

    contador = 1

    print(liderTabla(dictEquipos) + "\n")
    for key, value in dictEquipos.items():
        escritor.writerow(
            [contador, key, value["ganados"], value["empatados"], value["perdidos"], value["goles_favor"], value["goles_contra"], value["puntos"], value["diferencia_goles"]]
        )
        contador += 1
