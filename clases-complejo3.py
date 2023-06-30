class ejemplo():
    def publico(self):
        return "Soy un metodo publico, a la vista de todo"
    def __privado(self):
        return "Soy un metodo privado, para ti no existo"
objeto=ejemplo()
print(objeto.publico())
print(objeto.__privado())
