num = input("")

mensaje = ""

try:
    lnum = [int(n) for n in num]
except:
    print("")
    quit()

total = str(sum(lnum))

contador = 1

for n in lnum:
    if contador == len(lnum):
        mensaje += f"{n} = {total}"
    else:
        mensaje += f"{n} + "
        contador += 1
        
print(mensaje)