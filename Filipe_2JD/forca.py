import random

def jogar():
    print("#### Bem Vindo ao jogo de Forca!!!!!")
    
    palavras = []
    abrir = input("##### escreva o tema de seu interece: geral, animais, magia, profissoes, ciencia, numeros, automoveis, mitologia(lembre-se de não colocar caracteres especiais)\n")
    arquivo = open(abrir.lower() + ".txt", "r")
    
    for linha in arquivo:
        palavras.append(linha.strip())
    
    palavra = random.choice(palavras)

    letras_acertadas = []
    

    for letra in palavra:
        letras_acertadas.append("_")

    chances = 6
    acertou = False
    inforcou = False
    while(not acertou and not inforcou):
        print(letras_acertadas)
        index = 0
        chute = input(f"Você tem {chances} chances!!!! Digite a letra de seu interesse(lebre-se que nenhuma palavra terá acento)\n")
        for letra in palavra:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = chute.upper()
        
            index = index +1
        if letras_acertadas.count(chute.upper()) == 0:
            chances = chances-1

        if chances == 0:
            inforcou = True
            print("que pena :( você errou!!! A palavra era: ", palavra.upper())

        if letras_acertadas.count("_") == 0:
            acertou = True
            print("parabéns, você acertou! a palavra era: ", palavra.upper())

    print("##### Fim do Jogo :(")

        
if(__name__ == "__main__"):
    jogar()