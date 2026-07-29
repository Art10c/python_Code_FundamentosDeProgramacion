sesiones = [

    [1,181,9],
    [2,58,3],
    [3,90,9],
    [4,179,8],
    [5,160,3]
]

def clasificar_sesion(sesion):
    if sesion[1]>180 and sesion[2]>8:
        return "Alto"
    elif sesion[1]<60 or sesion[2]<3:
        return "Bajo"
    else:
        return "Medio"

for sesion in sesiones:
    clasificacion = clasificar_sesion(sesion)
    print(f"Usuario {sesion[0]} su clasificacion es {clasificacion}")