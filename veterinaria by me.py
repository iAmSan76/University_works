#Carlos Santiago Palacios Monroy

#Se crea la clase gato 
class gato():

    #creamos un metodo contstructor para las variables
    def __init__(self,nombre,edad,tipo,alimento):
        #Carga los parametros se iguala el parametro a la variable
        self.nombre=nombre
        self.edad=edad
        self.tipo=tipo
        self.alimento=alimento
        
#una variable de pregunta para que ingrese a mi ciclo
        
preg="SI"
#mientras que ingresen gatos a la veterinaria estara en un ciclo

while (preg=="si"or preg=="SI"):

    #se pregunta si ha ingresado un gato a la clinica
    preg=input("¿Ha ingresado un gato a la clinica?: ")
    #si ha ingresado 
    if(preg=="si"or preg=="SI"):
    
        nombre=input("Ingrese el nombre de su gato: ")
        edad=float(input("Ingrese la edad de su gato: "))
        alimento=input("Ingrese el alimento favorito de su gato: ")

        if edad < 1.0:
            
            tipo="cachorro"
            
        if edad >= 1:

            tipo="Adulto"

        gatico=gato(nombre,edad,tipo,alimento)
        #con .format se reemplazan los datos en donde este el corchete 
        print("El nombre de mi gato es: {}".format(gatico.nombre))
        print("La edad de mi gato es {} y es un {} ".format(gatico.edad,gatico.tipo))
        print("Su alimento favorito es {}".format(gatico.alimento))
   
