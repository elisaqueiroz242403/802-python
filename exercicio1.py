def imprimir_qualquer_coisa(*args):
    for item in args:
        print(item)

imprimir_qualquer_coisa('maça', 'natação', 'pastel')


# dar print com a chave

def imprimir_qualquer_coisa(**kwargs):
    for chave, valor in kwargs.items():
        print(chave + ':' + valor)

imprimir_qualquer_coisa(fruta='banana', nome='Karen')


    