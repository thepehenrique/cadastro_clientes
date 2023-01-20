import banco
import validar
import os

#limpar termial
def limpar():
    return os.system('cls' if os.name == 'nt' else 'clear')

#cadastrar usuario
def registro():
    limpar()
    nome = validar.nome()
    email = validar.email()
    senha = validar.senha()
    estado = validar.estado()
    profissao = validar.profissao()
    limpar()
    print()
    banco.cur.execute("SELECT * FROM usuarios WHERE Email = ? AND Senha = ?", (email, senha))
    verificar = banco.cur.fetchone()
    limpar()
    try:
        if email in verificar and senha in verificar:
            print('O usuário já possui cadastro')

    #elif nome == "" and email == "" and senha == "" and estado == "" and profissao == "":
       # print('Preencha todos os Campos')

    except:
        banco.cur.execute("""
        INSERT INTO usuarios(nome, email, senha, estado, profissao) VALUES(?, ?, ?, ?, ?)
        """,(nome, email, senha, estado, profissao))
        banco.conn.commit()
        print('Conta criada. Bem vindo(a)')
        print()

#logar
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

#mostrar todos os nomes dos usuarios cadastrados
def cadastros():
    limpar()
    banco.cur.execute('SELECT Nome, Estado, Profissao FROM usuarios')
    for linha in banco.cur.fetchall():
        print(linha)
    print()

#remover usuario
def remover():
    limpar()
    removeremail = validar.email()
    removersenha = validar.senha()
    print()
    banco.cur.execute('DELETE FROM usuarios WHERE Email = ? AND Senha = ?', (removeremail, removersenha))
    print('Cliente removido')

#remove todos os usuários
def remover_todos():
    limpar()
    print('[1] CONFIRMAR\n[0] CANCELAR')
    op = int(input(': '))
    if op == 1:
        banco.cur.execute('DELETE FROM usuarios')
        print('Cadastros removidos')
    elif op == 0:
        print('Cancelado')
    else:
        print('Informe um valor válido')

#menu
def menu():
    while True:
        print('[1] CADASTRAR')
        print('[2] LOGIN')
        print('[3] CADASTROS')
        print('[4] REMOVER CADASTRO')
        print('[5] REMOVER TODOS OS CADASTROS')
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
            elif opcao == 4:
                remover()
            elif opcao == 5:
                remover_todos()
            elif opcao == 0:
                break
            else:
                limpar()
                print('Insira uma opção válida.')

        except ValueError:
            print('Insira uma opção válida')
            print()
menu()