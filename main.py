import banco
import validar
import os

def limpar():
    return os.system('cls' if os.name == 'nt' else 'clear')

def registro():
    limpar()
    nome = validar.nome()
    email = validar.email()
    senha = validar.senha()
    estado = validar.estado()
    profissao = validar.profissao()
    limpar()
    print()
    if nome == "" and email == "" and senha == "" and estado == "" and profissao == "":
        print('Preencha todos os Campos')
    else:
        banco.cur.execute("""
        INSERT INTO usuarios(nome, email, senha, estado, profissao) VALUES(?, ?, ?, ?, ?)
        """,(nome, email, senha, estado, profissao))
        banco.conn.commit()
        print('Conta criada. Bem vindo(a)')
        print()

def login():
    limpar()
    emaillogin = validar.email()
    senhalogin = validar.senha()
    print()
    banco.cur.execute("SELECT * FROM usuarios WHERE Email = ? AND Senha = ?", (emaillogin, senhalogin))
    verificar = banco.cur.fetchone()
    limpar()
    try:
        if emaillogin in verificar and senhalogin in verificar:
            print('Seja Bem-vindo(a)!')
            print()
    except:
        print('Você não possui um cadastro.')
        print()

def cadastros():
    limpar()
    banco.cur.execute('SELECT Nome FROM usuarios')
    for linha in banco.cur.fetchall():
        print(linha)
    print()

def menu():
    while True:
        print('[1] CADASTRAR')
        print('[2] LOGIN')
        print('[3] CADASTROS')
        print('[0] SAIR')
        try:
            opcao = int(input("Informe uma opção: "))
            print()
            if opcao == 1:
                registro()
            elif opcao == 2:
                login()
            elif opcao == 3:
                cadastros()
            elif opcao == 0:
                break
            else:
                limpar()
                print('Insira uma opção válida.')

        except ValueError:
            print('Insira uma opção válida')
            print()
menu()