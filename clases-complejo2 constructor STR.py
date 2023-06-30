class cachorro():
    #No hay atributos y con el metodo constructor se le agregan los parametros
    #que se necesitan en este caso 2 parametros que son color y raza y siempre
    #tiene que estar el self
    
    def __init__(self,color,raza):
        #Carga los parametros se iguala el parametro a la variable
        self.color=color
        self.raza=raza
    def __str__(self):
        return """\
Raza:{}
color:{}""".format(self.raza,self.color)
        
#se asigna la clase cahorro a una variable perrito
perrito=cachorro("Marron claro","Bulldog")
#con .format se reemplazan los datos en donde este el corchete 
print("Este es un cachorro de la raza {} y es de color {} ".format(perrito.raza, perrito.color))
