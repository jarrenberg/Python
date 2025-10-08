"""
Ejercicio 19 — Convertidor de mayúsculas/minúsculas
Pide una frase y una opción:
a) Convertir a mayúsculas
b) Convertir a minúsculas
c) Capitalizar (solo primera letra en mayúscula)
Implementa funciones separadas para cada caso.
Pista: usa .upper(), .lower(), .capitalize().
"""
def menu ():
    print("Menu:")
    print("a. Convertir a mayusculas")
    print("b. Convertir a minusculas")
    print("c. Capitalizar (solo primera letra en mayuscula)")

def convertir_a_minusculas (s:str)->str:
    return s.lower()

def convertir_a_mayusculas (s:str)->str:
    return s.upper()

def capitalizar (s:str)->str:
    return s.capitalize()

def main():
    menu()
    accion = input("Introduzca una accion a realizar: ")
    cadena = input("Introduzca una cadena: ")
    if(accion.isalpha()):
        accion=accion.lower()
        match accion:
            case n if accion == "a":
                print(convertir_a_mayusculas(cadena))
            case n if accion == "b":
                print(convertir_a_minusculas(cadena))
            case n if accion == "c":
                print(capitalizar(cadena))
            case _: 
                print("no se ha introduido una accion valida en el menu")
    else:
        print("La accion introducida no es una letra")
        
main()