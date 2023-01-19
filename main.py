import banco
import validar

def registro():
    nome = validar.nome()
    email = validar.email()
    senha = validar.senha()
    estado = validar.estado()
    profissao = validar.profissao()
    print()
    if nome == "" and email == "" and senha == "" and estado == "" and profissao == "":
        print('Preencha todos os Campos')
    else:
        banco.cur.execute("""
        INSERT INTO usuarios(nome, email, senha, estado, profissao) VALUES(?, ?, ?, ?, ?)
        """,(nome, email, senha, estado, profissao))
        banco.conn.commit()
        print('Conta criada. Bem vindo(a)')

def login():
    emaillogin = validar.email()
    senhalogin = validar.senha()
    print()
    banco.cur.execute("SELECT * FROM usuarios WHERE Email = ? AND Senha = ?", (emaillogin, senhalogin))
    verificar = banco.cur.fetchone()
    try:
        if emaillogin in verificar and senhalogin in verificar:
            print('Seja Bem-vindo(a)!')
            print()
    except:
        print('Você não possui um cadastro.')
        print()

def menu():
    while True:
        print('[1] CADASTRAR')
        print('[2] LOGIN')
        print('[0] SAIR')
        opcao = int(input('Informe uma opção: '))
        print()
        if opcao == 1:
            registro()
        elif opcao == 2:
            login()
        elif opcao == 0:
            break
        else:
            print('Insira uma opção válida.')

menu()