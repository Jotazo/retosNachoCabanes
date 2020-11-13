
x = int(input(""))

while x != 0:
    
    y = int(input(""))
    mensaje = f"{y} = "
    
    while y != 1:
        
        for ix in range(2, y+1):
            
            if y % ix == 0:
                mensaje += str(ix) + " "
                y = int(y/ix)
                break
            
        if y == 1:
            print(mensaje)
            x -= 1
        