"""2. Queremos imprimir os últimos 3 itens da nossa lista para saber quais 
comprar.
"""
def imprimir_lista():
    lista_festa = ["bolo", "salada", "balões", "letreiro_feliz_aniversário", "refrigerante"]
    lista_tamanho = len(lista_festa)
    i = 0

    while i < 3:
        i += 1
        print(lista_festa[lista_tamanho - i] )

imprimir_lista()