# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

class Pessoa:
    def __init__(self, Nome, Sobrenome, Idade, CidadeNatal, Genero):
        self.nome = Nome
        self.sobrenome = Sobrenome
        self.idade = Idade
        self.cidadenatal = CidadeNatal
        self.genero = Genero
    def Visualizar(self):
        print(self.__dict__)

p1 = Pessoa('Camila', 'vitoria', 21, 'Diadema', 'Feminino')
p2 = Pessoa('Luciana', 'Ferreira', 49, 'Recife', 'Feminino')
p3 = Pessoa('Antonio', 'jose', 61, 'Diadema', 'Masculino')
p4 = Pessoa('Camomila', 'vitoria', 44, 'Diadema', 'Feminino')
p5 = Pessoa('Everton', 'Silva', 22, 'São Paulo', 'Masculino')
p6 = Pessoa('Pedro', 'Samuel', 26, 'São Bernado', 'Masculino')

p1.Visualizar()
p2.Visualizar()
p3.Visualizar()
p4.Visualizar()
p5.Visualizar()
p6.Visualizar()

Bd = [p1,p2,p3,p4,p5,p6]

