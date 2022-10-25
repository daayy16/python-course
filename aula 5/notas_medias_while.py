def notas_medias():
    notas = []
    alunos = []
    medias = []
    qtd_alunos = (int(input("Quantos alunos são? ")))
    qtd_materias = (int(input("Quantas matérias são? ")))
    while len(alunos) < qtd_alunos:
        alunos.append(input("\nInforme o nome do aluno: "))
        count = 0
        while count < qtd_materias:
            count += 1
            notas.append(float(input("Informe a nota do aluno: ")))

    i_aluno = 0 #indice contador de aluno
    indice_mt = 0 #indice contador de matéria
    while i_aluno < qtd_alunos:
        notas_aluno = []
        count = 0
        i_aluno += 1
        while count < qtd_materias:
            count += 1
            notas_aluno.append(notas[indice_mt])
            indice_mt += 1
        
        medias.append(sum(notas_aluno) / qtd_materias)

    i_aluno = 0 #indice contador de aluno
    while i_aluno < qtd_alunos:
        if medias[i_aluno] >= 7:
            print(f"O aluno {alunos[i_aluno]} foi APROVADO")
        else:
            print(f"O aluno {alunos[i_aluno]} foi REPROPROVADO")
        i_aluno += 1
    
    print(medias)

    alunos.sort()
    print(f"os alunos são {alunos}")

    valores = []
    repeticao = []
    
    for media in medias:
        if media not in valores:
            valores.append(media)
        else:
            repeticao.append(medias.count(media))
            print(f"\n {medias.count(media)} alunos tiveram a média {media}")

    if len(repeticao) == 0:
        print("\nNenhum aluno teve média igual!")




notas_medias()