class ejemplo():

    def __init__(self):
        self.__oculto="Me encuentro oculto en la clase"
    def publico(self):
        return"Soy un metodo publico, a la vista de todos"
    def __privado(self):
        print("soy metodo privado, para ti no existo")
    def get_oculto(self):
        return self.__oculto
    def set_oculto(self):
        self.__oculto=self.__privado()
    
objeto=ejemplo()
print (objeto.publico())
print (objeto._ejemplo__privado())
print (objeto.get_oculto())#se ven los ocultos
objeto.set_oculto()#cambia el atributo oculto
