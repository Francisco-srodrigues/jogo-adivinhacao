# Desenvolvedor: FSRodrigues
# Data de desenvolvimento: 16/01/2025
# Horário: 22:52
# Jogo simples de adivinhação, onde o jogador tenta descobrir qual número de 1 a 10 o programa escolheu com a função random
import random

# Função para inserir linhas decorativas no console
def linha():
    print('-' * 40)

# Programa Principal
# Definindo cores para mensagens no console(Apenas para terminais compatíveis.)
ACERTO = '\033[1;92m' # Verde para mensagens de acerto
ERRO = '\033[1;91m' # Vermelho para mensagens de erro
NORMAL = '\033[0m' # Reset para o estilo normal

while True:
    linha()
    while True:
        try:
            chute = int(input('Qual número eu escolhi, entre 1 e 10?\n'))
            if 1 <= chute <= 10:
                break
            else:
                print('Por favor, insira um número entre 1 e 10.')
        except ValueError:
            print('Entrada inválida. Por favor, insira um número inteiro.')

    num = random.randint(1, 10)
    linha()
    if chute == num:
        print(ACERTO, 'Você acertou!!!', NORMAL)
        print(f'Caraca!!!!!!\nEu escolhi {num} e você digitou {chute}.\nTem certeza de que não hackeou minha mente?')
    else:
        print(ERRO, 'Você errou!', NORMAL)
        print(f'Que pena!!\nEu escolhi {num}, mas você digitou {chute}.\nMais sorte da próxima vez.')

    linha()
    jogar_novamente = input('Deseja jogar novamente? (s/n): ').strip().lower()
    if jogar_novamente != 's':
        print('Obrigado por jogar!\nEspero que tenha se divertido!\nAté a próxima!.\nValerious Systems™')
        break