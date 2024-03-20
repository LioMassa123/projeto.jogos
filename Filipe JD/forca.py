import random

def jogar():
    print("#### Bem Vindo ao jogo de Forca!!!!!")

    palavraN = random.randint(1,10)

    letras_acertadas = []
    chances = 5

    if(palavraN == 1):
        palavra = "estrela"

    elif(palavraN == 2):
        palavra = "tigre"

    elif(palavraN == 3):
        palavra = "escola"
    
    elif(palavraN == 4):
        palavra = "magico"
    
    elif(palavraN == 5):
        palavra = "dragao"

    elif(palavraN == 6):
        palavra = "fogo"

    elif(palavraN == 7):
        palavra = "agua" 

    elif(palavraN == 8):
        palavra = "terra"

    elif(palavraN == 9):
        palavra = "ar"  

    elif(palavraN == 10):
        palavra = "extintor"         

    for letra in palavra:
        letras_acertadas.append("_")

    acertou = False
    inforcou = False
    while(not acertou and not inforcou):
        print(letras_acertadas)
        index = 0
        chute = input(f"Você tem {chances} chances!!!! Digite a letra de seu interece(lebre-se que nenhuma palavra terá acento)\n")
        for letra in palavra:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = chute.upper()
        
            index = index +1
        if letras_acertadas.count(chute.upper()) == 0:
            chances = chances-1

        if chances == 0:
            inforcou = True
            print("que pena :( você errou!!! A palavra era: ", palavra)

        if letras_acertadas.count("_") == 0:
            acertou = True
            print("parabéns, você acertou! a palavra era: ", palavra)

    print("##### Fim do Jogo :(")

        
if(__name__ == "__main__"):
    jogar()