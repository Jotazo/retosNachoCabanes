le_gustan = []
no_le_gustan = []

num_potitos = 1
ingrediente = ""

while num_potitos != 0:

    num_potitos = int(input(""))

    for ix in range(num_potitos):
        potito = input("") # Ej potito: 'SI: ternera cebolla pimiento FIN' ¡Max 10 ing!¡Max 20 chr por ing!
    
        if potito[0] == "S": # Quiere decir que es un potito que se comió

            for letra in potito[4:]:
                if letra == " ": 
                    le_gustan.append(ingrediente)
                    ingrediente = ""
                elif letra == 'F':
                    break
                else:
                    ingrediente += letra

        else: # Quiere decir que es un potito que no se comió

            for letra in potito[4:]:
                if letra == " ":
                    no_le_gustan.append(ingrediente)
                    ingrediente = ""
                elif letra == 'F':
                    break
                else:
                    ingrediente += letra

        le_gustan = list(set(le_gustan))
        no_le_gustan = list(set(no_le_gustan))
        ix = 0

        while no_le_gustan in le_gustan:
            if no_le_gustan[ix] in le_gustan:
                no_le_gustan.pop(ix)
            else:
                ix += 1

    no_le_gustan.sort()
    

    for ingrediente in no_le_gustan:
        print(ingrediente, end="")

            
