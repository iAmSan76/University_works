a=input("Escriba su cedula o DNI  ")


def verificacion(a):

    b=len(a)
    
    if b==8 and b==7:
        print("Su cedula es valida")
    else:
        print("Su cedula es indalida")
    
