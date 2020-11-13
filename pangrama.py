dic = {
    'a':0,
    'b':0,
    'c':0,
    'd':0,
    'f':0,
    'g':0,
    'h':0,
    'i':0,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':0,
    'p':0,
    'q':0,
    'r':0,
    's':0,
    't':0,
    'u':0,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0,
    }

def reseteo():
    for letra in dic.keys():
        dic[letra] = 0


numFrases = int(input(""))

pangrama = "SI"

lista_respuestas = []

while numFrases != 0:
    
    frase = input("")
    
    for letra in frase:
        if letra.lower() in dic:
            dic[letra.lower()] += 1
            
    for valor in dic.values():
        if valor == 0:
            pangrama = "NO"
            break
    
    lista_respuestas.append(pangrama)
    numFrases -= 1
    reseteo()
    pangrama = "SI"
    

for respuesta in lista_respuestas:
    print(respuesta)
    
    
    