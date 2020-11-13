x = input("")

numeros = [num for num in x if num not in '0.,']

strNumerador = ""

for num in numeros:
    strNumerador += num
    
numerador = int(strNumerador)

denominador = 0
if numerador <= 10:
    denominador = 10
elif numerador <= 100:
    denominador = 100
elif numerador <= 1000:
    denominador = 1000
else:
    denominador = 10000

reducible = True

contador = 1

while reducible:
    
    contador +=1
    
    if numerador % contador == 0:
        
        if denominador % contador == 0:
            numerador = int(numerador / contador)
            denominador = int(denominador / contador)
            contador = 1
        else:
            reducible = False
            
    elif numerador < contador:
        reducible = False
            
    

print(f"{numerador}/{denominador}")

