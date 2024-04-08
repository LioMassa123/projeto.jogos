#impotar a bibliotéca Random
import random

###definir uma função
def jogar():
    #imprimir palavras
    print("#### Bem Vindo ao jogo de Forca!!!!!")
    # definir a Array [] palavras
    palavras = []
    #abrir os aquirvos
    abrir = input("##### escreva o tema de seu interece: geral, animais, magia, profissoes, ciencia, numeros, automoveis, mitologia(lembre-se de não colocar caracteres especiais)\n")
    arquivo = open(abrir.lower() + ".txt", "r")
    
    #definir a palavra secreta
    for linha in arquivo:
        palavras.append(linha.strip())
    
    palavra = random.choice(palavras)

    letras_acertadas = []
    

    #percorre a palavra
    for letra in palavra:
        #adicionar os _ em cada letra da palavra
        letras_acertadas.append("_")

    ##definições de variáveis
    chances = 6
    acertou = False
    inforcou = False
    ##jogo em si
    while(not acertou and not inforcou):
        print(letras_acertadas)
        index = 0
        # verificar o chute do usuário
        chute = input(f"Você tem {chances} chances!!!! Digite a letra de seu interesse(lebre-se que nenhuma palavra terá acento)\n")
        # Percorre a palavra letra por letra
        for letra in palavra:
            #verificar se o usuário acertou
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = chute.upper()
        
        #Verifica a próxima letra
            index = index +1
        #verificação se o usuário errou
        if letras_acertadas.count(chute.upper()) == 0:
            chances = chances-1

        # Verificação se o usuário inforcou
        if chances == 0:
            inforcou = True
            print("que pena :( você errou!!! A palavra era: ", palavra.upper())

        # Veificação se o usuário acertou a palavra
        if letras_acertadas.count("_") == 0:
            acertou = True
            print("parabéns, você acertou! a palavra era: ", palavra.upper())

    # Finalização do jogo
    print("##### Fim do Jogo :(")

        
# Verificação se o arquivo foi convocado de forma direta
if(__name__ == "__main__"):
    jogar()