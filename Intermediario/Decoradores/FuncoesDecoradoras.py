# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def buildFun(func):
    def internal (*args,**kwargs) :
        print('Vou decorar')
        for arg in args:
            Is_String(arg)
        result = func(*args,**kwargs)
        print('Ok, tudo decorado')
        return result
    return internal

def inverte_string(string):
    return string[::-1]


def Is_String(param): 
    if not isinstance(param,str):
        raise TypeError('param deve ser uma string')

inverte_string_Checando_parametro = buildFun(inverte_string)
invertida = inverte_string_Checando_parametro('Luiz')
print(invertida)

