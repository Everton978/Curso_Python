"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)"""

'''Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.'''

'''Closure e funções que retornam outras funções'''

def criar_saudacao(saudacao,nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom dia','João')
s2 = criar_saudacao('Boa tarde','Maria')
 
print(s1)
print(s2()) #esse é o closure, pois a função saudar() está sendo retornada e chamada posteriormente.