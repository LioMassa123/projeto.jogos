import random

def jogar():
    print("#### Bem Vindo ao jogo de Forca!!!!!")

    palavraN = random.randint(1,10)

    if(palavraN == 1):
        palavra: "estrela"

    elif(palavraN == 2):
        palavra: "tigre"

    elif(palavraN == 3):
        palavra: "escola"
    
    elif(palavraN == 4):
        palavra: "magico"
    
    elif(palavraN == 5):
        palavra: "dragao"

    elif(palavraN == 6):
        palavra: "fogo"

    elif(palavraN == 7):
        palavra: "agua" 

    elif(palavraN == 8):
        palavra: "terra"

    elif(palavraN == 9):
        palavra: "ar"  

    elif(palavraN == 10):
        palavra: "estintor"         

    acertou= False
    inforcou= False
    while(not acertou and not inforcou):
        print("jogando...")
        

    print("##### Fim do Jogo :(")

if(__name__ == "__main__"):
    jogar()