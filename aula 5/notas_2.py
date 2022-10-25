def media_alunos():
    alunos = []
    notas = []
    alunos.append(input("Informe o nome do aluno: "))
    notas.append(float(input("Informe a nota do aluno: ")))
    notas.append(float(input("Informe mais uma nota do aluno: ")))
    notas.append(float(input("Informe mais uma nota do aluno: ")))
    notas.append(float(input("Informe mais uma nota do aluno: ")))
    alunos.append(input("\nInforme o nome de outro aluno: "))
    notas.append(float(input("Informe a nota do aluno: ")))
    notas.append(float(input("Informe mais uma nota do aluno: ")))
    notas.append(float(input("Informe mais uma nota do aluno: ")))
    notas.append(float(input("Informe mais uma nota do aluno: ")))
    alunos.append(input("\nInforme o nome de outro aluno: "))
    notas.append(float(input("Informe a nota do aluno: ")))
    notas.append(float(input("Informe mais uma nota do aluno: ")))
    notas.append(float(input("Informe mais uma nota do aluno: ")))
    notas.append(float(input("Informe mais uma nota do aluno: ")))

    media_1 = sum([notas[0], notas[1], notas[2], notas[3]]) / 4
    if media_1 >= 7:
        print(f"{alunos[0]} foi aprovado com a nota {media_1}")
    else:
        print(f"{alunos[0]} foi reprovado com a nota {media_1}")

    media_2 = sum([notas[4], notas[5], notas[6], notas[7]]) / 4
    if media_2 >= 7:
        print(f"{alunos[1]} foi aprovado com a nota {media_2}")
    else:
        print(f"{alunos[1]} foi reprovado com a nota {media_2}")

    media_3 = sum([notas[8], notas[9], notas[10], notas[11]]) / 4
    if media_3 >= 7:
        print(f"{alunos[2]} foi aprovado com a nota {media_3}")
    else:
        print(f"{alunos[2]} foi reprovado com a nota {media_3}")

    alunos.sort()
    print(f"os alunos são {alunos}")
    if media_1 == media_2 and media_2 == media_3:
        print("Todos os alunos tiveram médias iguais")
    elif media_1 == media_2 or media_1 == media_3 or media_2 == media_3:
        print("Dois alunos tiveram médias iguais")
    else:
        print("Nenhum aluno teve médias iguais")
media_alunos()