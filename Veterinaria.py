#encoding: utf-8

#Se crea una clase de gato.
class Gato():

    #Se crea su metodo constructor, el cual tiene nombre, edad y comida.
	def __init__(self,N,E,C):
		self.N=N
		self.E=E
		self.C=C
    #Se crea el metodo str el cual me imprime mis valores
	def __str__(self):
		return"""""".format(self.N,self.E,self.C)

#Se consideran unas varibles de control.
aux='si'
cont=0

#Mientras mi auxiliar sea si o SI para evitar errores, ejecute.
while((aux=='si')or(aux=='SI')):
    #Pregunte si estan estrando gatos
	aux=input("¿Ingreso un gato?:")

    #Si ingreso uno nuevo pregunte.
	if((aux=='si')or(aux=='SI')):
		cont=cont+1
		nombre=input('Digite el nombre:')
		edad=float(input('Digite la edad:'))
		comida=input('Digite las comida del gato:')

        #Luego de almacenar mis variables, creo un gato y le paso sus atributos
		gt=Gato(nombre,edad,comida)

        #Miro si mi gato es mayor de 1 año
		if(gt.E<1):
			my='no'
		else:
			my='si'
        #Imprimo la información de mi gato
		print (str(gt))
		print("El gato de nombre {} come {}, tiene {} años ".format(gt.N,gt.C,gt.E))
		print ("y "+str(my)+" mayor")
		print("\n")

#Cuando ya no entran más gatos, muestro en pantalla la cantidad de gatos que ingresaron a mi veterinaria.
print("Su veterinaria tiene "+str(cont)+" gatos")
