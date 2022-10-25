"""5. Faça um programa que leia 5 números e informe o maior número
"""
def max_number():
    i = 0
    list_number = []
    while i < 5:
        number = input("\nInsira um número: ")
        if not number.isnumeric():
            print("\nCaracter inválido: ")
        else:
            list_number.append(int(number))
            i += 1
    print(f"A lista é {list_number}")
    print(f"O maior número da lista é {max(list_number)}")

max_number()


