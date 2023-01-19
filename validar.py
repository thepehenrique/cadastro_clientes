def nome():
    while True:
        nome = input('Nome Completo: ')
        if nome == '':
            print('Entrada Vazia.')
            continue
        temp = ''.join(nome.split(' '))
        for i in temp:
            if i.isdigit():
                print('Digite um nome válido.')
                break
        else:
            return nome.strip(' ')
        
def email():
    while True:
        email = input('Email: ')
        if email == '':
            print('Entrada vazia.')
        elif '@' and '.com' in email:
            return email.strip(' ')
        else:
            print('Email Inválido')

def senha():
    while True:
        senha = input('Senha: ')
        if senha == '':
            print('Entrada vazia.')
            continue
        return senha.strip(' ')
    
def estado():
    while True:
        estado = input('Estado: ')
        if senha == '':
            print('Entrada vazia.')
            continue
        temp = ''.join(estado.split(' '))
        for i in temp:
            if i.isdigit():
                print('Digite um estado válido.')
                break
        else:
            return estado.strip(' ')

def profissao():
    while True:
        prof = input('Profissão: ')
        if prof == '':
            print('Entrada vazia')
            continue
        temp = ''.join(prof.split(' '))
        for i in temp:
            if i.isdigit():
                print('Digite um nome válido.')
                break
        else:
            return prof.strip(' ')
