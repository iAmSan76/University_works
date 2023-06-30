class cachorro():
    #No hay atributos y con el metodo constructor se le agregan los parametros
    #que se necesitan en este caso 2 parametros que son color y raza y siempre
    #tiene que estar el self
    
    def __init__(self,color,raza,id):
        #Carga los parametros se iguala el parametro a la variable
        self.color=color
        self.raza=raza
        self.id=id
    def __str__(self):
        return """\
Raza:{}
color:{}""".format(self.raza,self.color)
    def __repr__(self)->str:
        return"<cachorro {}>".format(self.id)
        
#se asigna la clase cahorro a una variable perrito
perrito=cachorro("Marron claro","Bulldog",1)
print(repr(perrito))
