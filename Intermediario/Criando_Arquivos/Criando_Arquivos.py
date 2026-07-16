# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

Arquivo = 'Teste01.txt' # o python ira criar o arquivo no mesmo local que o main

Caminho_completo = 'C:\\Cursos_Udemy_e_Hortmart\\Curso_Python\\Intermediario\\Criando_Arquivos\\'
Caminho_completo += 'Teste02.txt'

Texto = open(Caminho_completo,'w')
Texto.close()

#tambem possivel criar com com with
Caminho_completo=Caminho_completo.replace('Teste02.txt',Arquivo)

with open(Caminho_completo, 'w') as textin:
    print('Iniciando........')
    print(f"Seu Arquivo{Arquivo}está fechamdo,\n Obrigado!!!")