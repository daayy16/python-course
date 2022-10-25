"""4. Faça um programa que leia e valide as seguintes informações: Nome: 
maior que 3 caracteres; 
a.Idade: entre 0 e 150; 
b.Salário: maior que zero; 
c.Sexo: 'f' ou 'm'; 
d.Estado Civil: 's', 'c', 'v', 'd'; 
Use a função len(string) para saber o tamanho de um texto (número de 
caracteres).
"""
def person_information():
    name = ""
    age = -1
    salary = 0
    list_gender = ["f", "m"]
    gender = ""
    list_gender = ["f", "m"]
    marital_status = ""
    marital_list = ["s", "c", "v", "d"]
    while len(name) < 3:
        name = input("\nDigite seu nome: ")
    while age < 0 or age > 150:
        age = int(input("\nDigite sua idade: "))
    while salary <= 0:
        salary = float(input("\nDigite seu salário: "))
    while gender not in list_gender:
        gender = input("\nDigite seu sexo f para feminino e m para masculino: ")
    while marital_status not in marital_list:
        marital_status = input("\nDigite seu estado civil s para solteiro, c para casado, v para viúvo e d para divorciado : ")
    
    print(f"\nNome: {name} \nIdade: {age} \nSalário: {salary} \nSexo: {gender} \nEstado Civil: {marital_status}")

person_information()
    
