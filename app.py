import random

jogadas = ['pedra', 'papel', 'tesoura']
jogador = input("Escreva sua jogada\n")
computador = random.choice(['pedra', 'papel', 'tesoura'])

def jogarPedraPapelTesoura(jogador, computador):
        if computador == jogador:
            print('empate')
        elif jogador == 'pedra' and computador == 'tesoura':
            print('pedra vence')
        elif jogador == 'pedra' and computador == 'papel':
            print('papel vence')
        elif jogador == 'tesoura' and computador == 'papel':
            print('tesoura vence')
        elif jogador == 'tesoura' and computador == 'pedra':
            print('pedra vence')
        elif jogador == 'papel' and computador == 'tesoura':
            print('tesoura vence')
        elif jogador == 'papel' and computador == 'pedra':
            print('papel vence')
        else:
            print('jogada invalida')

jogarPedraPapelTesoura(jogador, computador)


from flask import Flask
app = Flask(__name__)
# write 'hello world' to the console
@app.route("/")
def hello():
    return app.send_static_file("index.html")
