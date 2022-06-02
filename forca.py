#planos: descobrir uma maneira de colocar níveis, variando as tentativas
#planos: dar dica sobre palavras

import random



def jogar():
    
    bem_vindo()

    
    palavra_secreta = funcao_palavra()

    letras_corretas = adiciona_caracter(palavra_secreta)
    print(letras_corretas)
    
    
    enforcou = False
    acertou  = False
    erros = 0
    
    
    while (not enforcou and not acertou):
        

        chute = pede_chute()
        if (chute in palavra_secreta):
            marcando_chute_correto(chute, letras_corretas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            

        enforcou = erros == 7 
        acertou = "_" not in letras_corretas
            
        print(letras_corretas)
    

    if acertou:
         vencedor()
    else: 
        perderdor(palavra_secreta)

        print("Fim do game")

def vencedor():
    print("Voce ganhou, parábens.")
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    

def perderdor(palavra_secreta):
    print(f"Voce perdeu, a palavra era {palavra_secreta}")
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def marcando_chute_correto(chute, letras_corretas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
            if (chute == letra): 
                letras_corretas [posicao] = letra
            posicao +=1 

def pede_chute():
    chute = input("Insira sua letra: ")
    chute = chute.strip().upper() #retira os espaços em brancos
    return chute

def bem_vindo():
    jogador = input("Qual o seu nome? ")
    jogador = jogador.title()
    print("*************************************")
    print(f"Bem vindo ao jogo da forca, {jogador}")
    print("*************************************")
    print("Lembrando que as palavras não tem acentos.")
    

def funcao_palavra():
    arquives = open("palavras.txt", "r")
    palavra = []

    for linha in arquives:
        linha = linha.strip()
        palavra.append(linha)

    #text = arquives.read()
    #print(text)
    arquives.close()
    numero_aleatorio = random.randrange(0, len(palavra))
    palavra_secreta = palavra[numero_aleatorio].upper()
    palavra_secreta = palavra[numero_aleatorio].upper()
    #letras_corretas =  #list comprehension
    #for letras in palavra_secreta: Outra maneira de fazer.
        #letras.append("_")
    return palavra_secreta

def adiciona_caracter(palavra_secreta):
    return ["_" for letras in palavra_secreta]

if (__name__== "__main__"):
    jogar()