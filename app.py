import random

pontuacao_jogador = 0
pontuacao_computador = 0

def abrirTeclado():
    jogador = input("Escreva sua jogada\n")
    jogador = jogador.lower()
    return jogador

def jogarPedraPapelTesoura(jogador):
    global pontuacao_jogador
    global pontuacao_computador

    computador = random.choice(['pedra', 'papel', 'tesoura'])

    if computador == jogador:
        print('empate')
    elif jogador == 'pedra' and computador == 'tesoura':
        pontuacao_jogador += 1
        print('pedra vence')
    elif jogador == 'pedra' and computador == 'papel':
        pontuacao_computador += 1
        print('papel vence')
    elif jogador == 'tesoura' and computador == 'papel':
        pontuacao_jogador += 1
        print('tesoura vence')
    elif jogador == 'tesoura' and computador == 'pedra':
        pontuacao_computador += 1
        print('pedra vence')
    elif jogador == 'papel' and computador == 'tesoura':
        pontuacao_computador += 1
        print('tesoura vence')
    elif jogador == 'papel' and computador == 'pedra':
        pontuacao_jogador += 1
        print('papel vence')
    else:
        print('jogada invalida')

def exibirPontuacaoFinal():
    print("Pontuação do jogador: ", pontuacao_jogador)
    print("Pontuação do computador: ", pontuacao_computador)

def jogarNovamente():
    while True:
        continuar = input("Deseja jogar novamente?\n")
        continuar = continuar.lower()
        if continuar == 'sim':
            jogarPedraPapelTesoura(abrirTeclado())
        else:
            exibirPontuacaoFinal()
            print("Obrigado por jogar!")
            break

jogarPedraPapelTesoura(abrirTeclado())

jogarNovamente()

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")
