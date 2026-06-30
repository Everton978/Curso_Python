#Aulas sobre o tipo lista;

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

"""
#posso ter quase todos os tipos inclusive outras listas


#------- -4- -3 -2-- -1 
#---------0---1--2----3 
lista = [10, 20, 30, 40]
print(lista,type(lista[2]))

#Posso alterar sobreescrevendo valores : e.g
lista[-3] = 4.004
print(lista, type(lista[-3]))

lista[1] = "A"
print(lista, type(lista[1]))

#posso apagar determinado idice, alto custo computacional em listas muito grandes
del lista[0]
print(lista,'Removido,',lista[0],type(lista[0]))

#Posso adicionar algo no final,comando append
lista.append(40.556) # adiciona ao final quantas vezes eu  quiser
lista.append('BCC')
lista.append(4)
print(lista)

#Posso remover o ultimo item da minha lista .pop
Ultimo_valor = lista.pop
print(lista, 'Removido,',Ultimo_valor)

#Posso Limpar toda a minha lista, comando clear
lista.clear()
print(lista)

lista = [10, 20, 30, 40,50,60,80,90,100]
print(lista)

# posso adicionar um intem em um indice específico, comando insert
lista.insert(2, 300) # indice 2 recebe o valor 300, os outros itens são deslocados para a direita
print(lista)

# A concatenação de listas é possível, sendo ela polimofica, comando extend ou operador +
listab = [1, 2, 3]
listaC = lista + listab
print(listaC)
Lista_D = lista.extend(listab) # o comando extend não retorna nada, ele modifica a lista original
lista.append(listaC) # o comando append adiciona a listaC como um item da lista, ou seja, a listaC é adicionada como um item da lista
print(lista)