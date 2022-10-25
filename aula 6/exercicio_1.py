"""1. Suponha que o supermercado só tenha produtos com mais de 6 caracteres em seu 
nome. Imprima lista_festa produtos que atendam a essa condição."""
def retorno_lista_festa():
    lista_festa = ["bolo", "salada", "balões", "letreiro_feliz_aniversário", "refrigerante"]
    for lista in lista_festa:
        if len(lista) > 6:
            print(lista)

retorno_lista_festa()