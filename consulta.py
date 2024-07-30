from compositores import compositores


def edad():
    while True:
        nombre_compositor = input(
            f"Ingrese un Compositor (o 'salir' para terminar): ").capitalize()
        if nombre_compositor == "SALIR":
            break
        if nombre_compositor in compositores:
            nacimiento = compositores[nombre_compositor]["nacimiento"]
            if "muerte" in compositores[nombre_compositor]:
                muerte = compositores[nombre_compositor]["muerte"]
                edad = muerte - nacimiento
                print(f"La edad de {nombre_compositor} era {edad} años")
            else:
                print(f"No se encuentra registrada la fecha de muerte de {
                      nombre_compositor}")
        else:
            print("Compositor no encontrado")


edad()
