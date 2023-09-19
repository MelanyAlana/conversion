from form.formulas import Radianes, Grados

def main():
    opcion = input("¿Deseas ingresar el ángulo en grados (G) o radianes (R)? ").upper()

    if opcion == "G":
        grados = float(input("Ingrese el valor en grados: "))
        angulo = Grados(grados)
        print(f"{grados} grados son equivalentes a {angulo.a_radianes()} radianes.")
    elif opcion == "R":
        radianes = float(input("Ingrese el valor en radianes: "))
        angulo = Radianes(radianes)
        print(f"{radianes} radianes son equivalentes a {angulo.a_grados()} grados.")
    else:
        print("Opción no válida. Por favor, ingresa 'G' o 'R'.")

if __name__ == "__main__":
    main()