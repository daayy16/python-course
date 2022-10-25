#1. Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar

def even_or_odd():
    number = int(input("Escreva um número: "))
    if (number % 2 == 0):
        print("O número", number, "é par!")
    else:
        print("O número", number, "é impar!")

even_or_odd()