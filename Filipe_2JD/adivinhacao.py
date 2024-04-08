#importar a biblioteca random
import random

# Difinir a função jogar
def jogar():
    print("########## seja bem vindo ao JOGO DE ADIVINHAÇÃO!!!!!!")
    #definição das dificuldades
    dificuldade =int(input("selecione a dificuldade: 1-fácil (7 tentativas); 2-médio (5 tentativas), 3-difícil (3 tentivas); 4-impossível! (1 tentativa) \n"))

    #definir a dificuldade fácil
    if (dificuldade == 1):
        max_tentativa = 7

    #definir a dificuldade médio
    elif (dificuldade == 2):
        max_tentativa = 5

    #definir a dificuldade difícil
    elif (dificuldade == 3):
        max_tentativa = 3

    #definir a dificuldade impossível
    elif (dificuldade == 4):
        max_tentativa = 1

    #verificar dificuldade inválida
    else :
        print("dificuldade inválida!")

    #sortear o número
    sorteio = random.randint(0,10)




    # jogo em si
    for i in range(max_tentativa) :
        #Verificação do chute do usuário
        chute = int(input(f"você tem {max_tentativa} tentativa(s) - faça seu chute!, entre 0 a 10: \n"))
        #definição das variáveis
        acertou = chute == sorteio
        menor = chute < sorteio
        maior = chute > sorteio
        #verificar se o usuário acertou
        if(acertou):
            print("parabéns! Você ganhou!!!! O número era: ", sorteio)
            break
        
        #verificar se o usuário chutou um número menor
        elif(menor):
            print("o número sorteado é maior que", chute)
        
        #verificar se o usuário chutou um número maior
        elif(maior):
            print("o número sorteado é menor que", chute)
        

    #verificação do acerto do jogador
    if(acertou == 0):
        print("####### O Jogo acabou :( o número era: ", sorteio)
        
# Verificação se o arquivo foi convocado de forma direta
if(__name__ == "__main__"):
    jogar()    