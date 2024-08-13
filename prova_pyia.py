# PYIA-A02] Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. 
# Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone 
# e o endereço de email. Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, 
# mostrando todas as informações do contato inserido pelo usuário.

contato = {}

for _ in range(4): #supondo que seja mais de um cadastro, por isso o range (4).
    numero = []
    email = []
    nome= input('Digite o nome do Contato:')
    for _ in range(1):
          numero.append(int(input('Digite o numero de telefone:')))
          email.append(input('Digite o e-mail:'))
    
    contato[nome]={'numero': numero,'e-mail':email}
    
    for nome,cadastro in contato.items():
        print(f'Nome:{nome}')
        for numero,email in cadastro.items():
            print(f'{numero}:{email}')
        
        
            