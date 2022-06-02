''' Ex1
from math import sqrt


class Rocket():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment

    def print_rocket(self):
        print(self.x, self.y)

foguete = Rocket(15,25)
foguete.print_rocket()

foguete.move_rocket(-5,17)
foguete.print_rocket()
'''

'''Ex2
class Pessoa():
    def __init__(self, nome, cidade, telefone, email, idade):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        self.idade = idade

    def __str__(self):
        return self.nome

    def __len__(self):
        return self.idade

alan = Pessoa('Alan','Udia','(34)99798556','mail.alan@checkup.com',30)
print(alan)
'''


# Ex 3

class Smartphone():

    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface


class MP3(Smartphone):

    def __init__(self, tamanho, interface, capacidade):
        super().__init__(tamanho, interface)
        self.capacidade = capacidade
        print('MP3 criado!')


mp3 = MP3('12', 'Android', '16')