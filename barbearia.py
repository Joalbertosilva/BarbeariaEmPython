from principal import menu, servico, marcar_horario, register, login, mostrar_hora_marcada, visualizarCliente

servicos = {'Cabelo, corte normal':15,
            'Cabelo e sobrancelha': 20,
            'Cabelo, sobrancelha e barba': 35,
            'Sobrancelha': 7,
            'Barba': 15,
            'Cabelo e barba': 30,
            'Barbaterapia e cabelo': 50,
            'Platinar e corte': 100
            }
def inicio():
    try:
        while True:
            print('''
|---------------------------------------------------|                                                   
|1. Cadastro                                        |
|2. Login                                           |
|3. Ver clientes                                    |
|4. Sair                                            |
|                                                   |
|---------------------------------------------------|''')
            opcao = int(input('Escolha uma das opções acima: '))
            menu(opcao)
            if opcao == 1:
                cadastro()
            elif opcao == 2:
                meioFinal()
            elif opcao == 3:
                 ver_cliente()
           
    except ValueError:
        print()
        print('Por favor nos informe sua escolha através de numeros, escolha [1 / 2 / 3 ou 4], não digite nenhuma palavra ou letra.')
        print()
        inicio()

def ver_cliente():
    nome = input('Insira seu nome: ')
    senha = input('Insira sua senha: ')
    visualizarCliente(nome, senha)

def cadastro():
    usuario = input('Digite um e-mail ou nome de usuário para salvar seus cortes: ')
    senha = input('Crie sua senha: ')
    print("Usuário cadastrado com sucesso!")
    print()
    register(usuario, senha)

def entrar():
    usuario = input('Digite seu e-mail ou nome de usuário para acessar a página: ')
    senha = input('Insira sua senha: ')
    login(usuario, senha)
    if login(usuario, senha):
        print('Acesso permitido.')
    else:
        print()
        print('Acesso negado. Tente novamente')
        print()
        entrar()
def meioFinal():        
    try:    
            print()
            entrar()
            barber1 = 'João Alberto'
            barber2 = 'Guilherme Alencar'
            print()
            nome = input('Insira seu nome por favor: ')
            selecionar = int(input(f'\nQual dos barbeiros fará o serviço [1 - {barber1} / 2 - {barber2}]? '))
                
            print(f'\nMuito bem {nome} escolha um serviço por favor:')
            escolha = int(input('''\nEsolha um dos serviços abaixo: 
            1. Cabelo, corte normal: R$15
            2. Cabelo + sobrancelha: R$20
            3. Cabelo + Barba: R$30
            4. Cabelo + Sobrancelha + Barba: R$35
            5. Sobrancelha: R$7 
            6. Barba: R$15
            7. Barbaterapia + Corte: R$50
            8. Platinar + Corte: R$100
            : ''')) 
            servico(nome, selecionar, barber1, barber2, escolha)
                
            mostrar_hora_marcada()
            dia = input('''
                Escolha o dia: 
                1 - Segunda
                2 - Terça
                3 - Quarta
                4 - Quinta
                5 - Sexta
                : ''')
            horario = input('''
                Escolha agora o horário: 
                1 - 09:00
                2 - 10:00
                3 - 11:00
                4 - 12:00
                : ''')
            marcar_horario(dia, horario)
    except ValueError:
        print('Por favor, informe sua escolha através de números, não digite palavras ou letras.')
        print()
        
inicio()