import random

print("########## seja bem vindo ao JOGO DE ADIVINHAÇÃO!!!!!!")
dificuldade =int(input("selecione a dificuldade: 1-fácil (7 tentativas); 2-médio (5 tentativas), 3-difícil (3 tentivas); 4-impossível! (1 tentativa) \n"))

if (dificuldade == 1):
    max_tentativa = 7

elif (dificuldade == 2):
    max_tentativa = 5

elif (dificuldade == 3):
    max_tentativa = 3

elif (dificuldade == 4):
    max_tentativa = 1

else :
    print("dificuldade inválida!")

sorteio = random.randint(0,10)




for i in range(max_tentativa) :
    chute = int(input(f"você tem {max_tentativa} tentativa(s) - faça seu chute!, entre 0 a 10: \n"))
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
    

if(acertou == 0):
    print("####### O Jogo acabou :( o número era: ", sorteio)    