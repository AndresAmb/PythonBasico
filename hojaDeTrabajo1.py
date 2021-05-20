peso=float(input("Ingrese su peso en kg:"))
estatura=float(input("Ingrese su estarura en m: "))
masaCorporal=round(peso/estatura**2,2)
print("Su masa corporal es: "+ str(masaCorporal))