class coche():
    ruedas=4
    velocidad=80
    def desplazamiento(self):
        print("El coche se esta desplazando sobre 4 ruedas")
        print("El coche tiene una velocidad de 80km/h")
        
miVehiculo=coche()
print("Mi coche tiene ",miVehiculo.ruedas,"ruedas")
print("Mi coche tiene una ",miVehiculo.velocidad,"km/h")
miVehiculo.desplazamiento()

