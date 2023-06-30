#Carlos Santiago Palacios Monroy

#Se crea una funcion para validar si el DNI es correcto
def DNI_Valido(DNI,nombre,apellido):
    #Se valida si el DNI ingresado tiene 7 o 8 digitos para esto usamos len
    if len(DNI)==7 or len(DNI)==8:
        #Si es valido enviamos lo datos a la funcion de suma
        suma(DNI,nombre,apellido)
        pass
    #sino no tiene 7 o 8 digitos entra en el bucle infinito
    else:
        #sino es valido entra en un bucle infinito con una contadora
        cont=0
        while cont==0:
            #se vuelve a pedir un DNI ya que el inicial estaba incorrecto no tenia entre 7 o 8 digitos
            DNI2=input("ESCRIBA UN DNI CORRECTO:  ")
            #creo una variable para comparar
            DNI=DNI2
            #indico que recibe un dato de tipo string para que no tenga problemas
            str('DNI')
            #se valida de nuevo pero con un dato nuevo
            if len(DNI2)==8 or len(DNI2)==7:
                #si es valido entonces saldra del ciclo sumando uno
                cont+=1
                #se envia de nuevo los datos
                suma(DNI,nombre,apellido)

        
# Se crea una funcion llamada suma para los tres primero digitos del DNI y para escribir los datos        
def suma(DNI,nombre,apellido):
    #se crea un for para la posicion de cada uno de los 3 digitos
    for i in DNI:
        a=DNI[0]
        b=DNI[1]
        c=DNI[2]
    #se crea una variable para el conteo total del apellido    
    cont_apellido=len(apellido)
    #se suman todos los datos para mostrarlos 
    total=nombre+str(cont_apellido)+a+b+c
    #Muestra los datos
    print("****SUS DATOS SON****")
    print("NOMBRE: ",nombre,nombre2,apellido)
    print("DNI: ",DNI)
    print(total)
    
    
#se solicitan los datos
preg=0
#Entra en un bucle que preguntara cada vez el nombre hasta que oprima enter
while preg==0:
    #solicitamos un nombre
    print("***SI DESEA SALIR PULSE ENTER CUANDO SE LE SOLICITE SU NOMBRE***\n")
    nombre=input("ESCRIBA SU NOMBRE:  ")
    #se le pregunta si es enter o un espacio lo que dejo entonces saldra del sistema
    if nombre=='':
        #Sumara 1 y ya no tendra que volver a entrar al ciclo
        preg+=1
        print("***SU SERVICIO HA FINALIZADO***")
    #Se crea un if para preguntar los otros datos
    if(preg==0):
        print("***SI NO TIENE SEGUNDO NOMBRE PULSE ENTER***\n")
        nombre2=input("ESCRIBA SU SEGUNDO NOMBRE:  ")
        apellido=input("ESCRIBA SU APELLIDO:  ")
        #Se piden los datos del DNI y se envian a la funcion de validacion
        DNI=input("ESCRIBA SU DNI:  ")
        DNI_Valido(DNI,nombre,apellido)
        DNI='000'
        

