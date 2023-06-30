#Carlos Santiago Palacios Monroy

# define una funcion para determinar la palabra final
def final(oracion):
    #inicializamos una variable contadora
    #para mirar la cantidad de digitos de la ultima palabra
    cont=0
    #Creamos un ciclo for para buscar la ultima palabra con
    #la funcion range y len para escribir mi cadena en un rango de numeros
    for i in range(len(oracion)):
        #Se crea un if para eliminar los espacios de la oracion
        if oracion[i]!=' ':
            
            cont+=1
        #sino hay un espacio entonces creamos un else anidado de un if en donde se
        #compara si mi variable sumadora "i" es menor a el total de la cadena -1
        #espacio que se retiro y a la posicion se le sumara 1 si no tiene espacio
        else:
            #se eliminaran posiciones en el rango hasta que ya no hallan mas espacios ni mas palabras excepto la ultima posicion 
            #Asi mismo se eliminan las palabras que no sean de la ultima posicion validando el ultimo espacio
           if i<len(oracion)-1 and oracion[i+1]!=' ':
               #se iguala mi contador a 0 
               cont=0
               
    #se muestra la cantidad de digitos de la uñtima palabra      
    print ("La cantidad de digitos de su ultima palabra es: ",cont)
    #retorna a cont
    return cont
    
#se solicitan los datos     
texto=input("Digite su oracion: ")
#se envian los datos a la funcion
final(texto)


    
