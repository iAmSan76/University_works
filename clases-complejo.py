
class coche():#molde
    ruedas=4
    velocidad=80#atributos
    def desplazamiento(self):#Metodo o funcion
        print("El coche se esta desplazando sobre 4 ruedas")
        print("El coche tiene una velocidad de 80km/h")
        
miVehiculo=coche()
print("Mi coche tiene ",miVehiculo.ruedas,"ruedas")
print("Mi coche tiene una ",miVehiculo.velocidad,"km/h")
miVehiculo.desplazamiento()

#solo cambia la clase SI se cambian los atributos
class moto():#mismo molde, cambia solo el objeto pero sigue siendo una clase
    ruedas=2
    velocidad=60#mismos atributos
    def desplazamiento(self):#mismo metodo
        print("La moto se esta desplazando sobre 2 ruedas")
        print("La moto tiene una velocidad de 60km/h")
        
#declaracion segundo objeto   
miVehiculo2=moto()
print("Mi coche tiene ",miVehiculo2.ruedas,"ruedas")
print("Mi coche tiene una ",miVehiculo2.velocidad,"km/h")
miVehiculo.desplazamiento()
