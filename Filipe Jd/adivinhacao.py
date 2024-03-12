import random

print("########## seja bem vindo ao JOGO DE ADIVINHAÇÃO!!!!!!")
dificuldade =int(input("selecione a dificuldade: 1-fácil (7 tentativas); 2-médio (5 tentativas), 3-difícil (3 tentivas); 4-impossível! (1 tentativa) \n"))

if (dificuldade == 1):
    tentativa = 7

elif (dificuldade == 2):
    tentativa = 5

elif (dificuldade == 3):
    tentativa = 3

elif (dificuldade == 4):
    tentativa = 1

else :
    print("dificuldade inválida!")

sorteio = random.randint(0,10)




for i in range(tentativa) :
    chute = int(input(f"você tem {tentativa} tentativa(s) - faça seu chute!, entre 0 a 10: \n"))
    acertou = chute == sorteio
    menor = chute < sorteio
    maior = chute > sorteio
    if(acertou):
        print("parabéns! Você ganhou!!!! O número era: ", sorteio)
        break
    
    elif(menor):
        print("o número sorteado é maior!")
    
    elif(maior):
        print("o número sorteado é menor!")
    
    tentativa = tentativa-1

if(acertou == 0):
    print("####### O Jogo acabou :( o número era: ", sorteio)    