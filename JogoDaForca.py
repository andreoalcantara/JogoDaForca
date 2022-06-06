#=========================================JOGO DA FORCA=========================================
import random

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    f = open('palavras.txt','r')
    f = f.read()
    f = f.split(',')
    posi = random.randint(0,len(f)-1)
    print(f[posi])
    return (f[posi])

tabuleiro = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman:

    # Construtor
    def __init__(self, word):
        self.word = word
        self.missed_letters = list()
        self.right_letters = list()

    # Método para tentativa de letra
    def guess(self, letter):
        letter = letter.lower()
        if letter in self.word and letter not in self.right_letters:
            self.right_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else: return False
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters)==6)

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():return True
        else:return False

    # Método para não mostrar a letra no tabuleiro
    def hide_word(self):
        aux =''
        for letter in self.word:
            if letter not in self.right_letters:
                aux += '_'
            else: aux += letter
        return aux

    # Método para checar o status do game e imprimir o tabuleiro na tela
    def print_game_status(self):
        print(tabuleiro[len(self.missed_letters)])
        print('Palavra: ' + self.hide_word())
        print('Letras erradas: ')
        for letter in self.missed_letters:
            print(letter)


# Função para ler uma palavra de forma aleatória do banco de palavras


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        print('\n')
        letra_usuario = input('Digite uma letra: ')
        game.guess(letra_usuario)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print(25*'-=')
        print(20*" "+'Você venceu!!')
        print(25 * '-=')
    else:
        print(25 * '-=')
        print(20*" "+'Você perdeu!!.')
        print(25 * '-=')
        print('A palavra era ' + game.word)



# Executa o programa
if __name__ == "__main__":
    main()