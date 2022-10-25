"""3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma 
mensagem caso o valor seja inválido e continue pedindo até que o 
usuário informe um valor válido. """
def insert_note():
    notes_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    note = input("\nInsira uma nota entre 0 e 10: ")
    if not note.isdigit():
        invalid_character()
    else:
        while int(note) not in notes_list:
            invalid_character()
        print(f"A nota é {int(note)}")

def invalid_character():
    print("A nota inserida não é valida!")
    insert_note()

insert_note()