print("Si desea salir presione 0")
print(" ")
i=input("Ingrese su numero entero  ")
comp=int(i)
par=0
tpar=0
impar=0
timpar=0
while comp != 0 and comp >=0 :
    for n in i:
        
        if int(n)%2==0:
            par=par+1
            tpar=tpar+1
        else :
            impar=impar+1
            timpar=timpar+1

    print("Su numero es: ",comp)
    print("la cantidad de digitos pares es: ",par)
    print("la cantidad de digitos impares es: ",impar)
    
    i=input("Ingrese su numero entero  ")
    comp=int(i)
    
    if comp==0:
        print("La cantidad total de digitos pares es: ",tpar)
        print("La cantidad total de digitos impares es: ",timpar)
    
        
    



