def imprimir_qualquer_coisa(*args):
    for numero,item in enumerate(args): 
        print(str(numero)+ '.' + item)

imprimir_qualquer_coisa('maça', 'natação', 'pastel')

# Para colocar o numero no elemento basta usar enumerate


 # dar print com a chave

def imprimir_qualquer_coisa(**kwargs):
     for chave, valor in kwargs.items():
         print(chave + ':' + valor)

 imprimir_qualquer_coisa(fruta='banana', nome='Karen')


    