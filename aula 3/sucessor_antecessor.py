#3. Desenvolva um programa que leia um número inteiro qualquer e que apresente o número informado, seguido do seu antecessor e do seu sucessor
number = int(input("Escolha um número: "))
n_antecessor = number - 1
n_sucessor = number + 1

print(f"O antecessor de {number} é {n_antecessor} e o seu sucessor é {n_sucessor}")
print("O antecessor de \033[35m", number, "\033[0mé\033[35m", n_antecessor, "\033[0me o seu sucessor é\033[35m", n_sucessor, "\033[0m")