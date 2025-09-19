# 8. Escribe un programa que recoja un mes del año (en número) y devuelva el número de días que tiene el mes. En caso de indicar un mes incorrecto deberá mostrar un mensaje de error.
mes = input("Introduce el mes:")
match mes:
    case n if mes=="Enero":
        print("El mes tiene 31 dias")
    case n if mes=="Febrero":
        print("El mes tiene 28 dias")
    case n if mes=="Marzo":
        print("El mes tiene 31 dias")
    case n if mes=="Abril":
        print("El mes tiene 30 dias")
    case n if mes=="Mayo":
        print("El mes tiene 31 dias")
    case n if mes=="Junio":
        print("El mes tiene 30 dias")
    case n if mes=="Julio":
        print("El mes tiene 31 dias")
    case n if mes=="Agosto":
        print("El mes tiene 31 dias")
    case n if mes=="Septiembre":
        print("El mes tiene 30 dias")
    case n if mes=="Octubre":
        print("El mes tiene 31 dias")
    case n if mes=="Noviembre":
        print("El mes tiene 30 dias")
    case n if mes=="Diciembre":
        print("El mes tiene 31 dias")
    case _:
        print("El mes no es valido")



