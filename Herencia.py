class padre():
    cabello="negro"
    ojos="azul"
    def conducir_coche(self):
        print("La persona sabe conducir coches")

class hijo(padre):
    def conducir_moto(self):
        print("La persona sabe manejar moto")

persona=hijo()
print(persona.cabello)
print(persona.ojos)
persona.conducir_coche()
persona.conducir_moto()
