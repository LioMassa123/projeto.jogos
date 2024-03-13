import adivinhacao
import forca

jogo = int(input("escolha o jgo desejado: 1-adivinhação; 2-forca \n"))

if(jogo==1):
    adivinhacao.jogar()
else:
    forca.jogar()    