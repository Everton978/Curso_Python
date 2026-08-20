##==========================================================#
#usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def buildFun(func):
    def internal (*args,**kwargs) :
        print('Vou decorar')
        for arg in args:
            Is_String(arg)
        result = func(*args,**kwargs)
        print('Ok, tudo decorado')
        return result
    return internal

@buildFun
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def Is_String(param): 
    if not isinstance(param,str):
        raise TypeError('param deve ser uma string')

invertida = inverte_string('MeuDeus')
print(invertida)