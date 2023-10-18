import sys
    
def marcar_horario(dia, horario):
    #Foi necessário abrir o caminho dentro da pasta salva para localizar o arquivo txt
    with open("C:\\Users\\joaob\\OneDrive\\Documentos\\BarbeariaFinal\\horarios.txt", "a+", encoding="utf-8" , errors="ignore") as arquivo:
        dias_semana = {
            '1': 'Segunda-feira',
            '2': 'Terça-feira',
            '3': 'Quarta-feira',
            '4': 'Quinta-feira',
            '5': 'Sexta-feira',
        }

        horarios_disponiveis = {
            '1': '09:00',
            '2': '10:00',
            '3': '11:00',
            '4': '12:00',
        }

        dia_escolhido = dias_semana.get(dia)
        horario_escolhido = horarios_disponiveis.get(horario)
        horario_marcado = (f"{dia_escolhido}:{horario_escolhido}")

        arquivo.seek(0)  # Volta para o início do arquivo para ler os horários marcados

        # Verificar se o horário já foi marcado
        if (f'{horario_marcado}\n') in arquivo.readlines():
            print(f"Horário {horario_marcado} já está marcado. Escolha outro horário.")
            remarcar()
        else:
            print('Horario marcado com sucesso. Aguardamos você.')
            print()
            arquivo.write(f'{horario_marcado}\n')
            # ... (seu código para escrever nos arquivos)
            with open("user.txt", "a+") as arquivo1:
                arquivo1.write(f'{dia_escolhido}:{horario_escolhido}\n')
            with open('horariosIndisponiveis.txt', 'a+', encoding="utf-8" , errors="ignore") as arquivo2:
                arquivo2.write(f'O horário {horario_escolhido} na {dia_escolhido} está indisponível.\n')
def remarcar():
    dia = input('''Escolha novamente o dia: 
                        1 - Segunda
                        2 - Terça
                        3 - Quarta
                        4 - Quinta
                        5 - Sexta
                        : ''')
    horario = input('''Escolha outro horário: 
                        1 - 09:00
                        2 - 10:00
                        3 - 11:00
                        4 - 12:00
                        : ''')
    marcar_horario(dia, horario)    
# Exemplo de uso:
def mostrar_hora_marcada():
    #Função para salvar as horas marcadas
    #Foi necessário abrir o caminho dentro da pasta salva para localizar o arquivo txt
    with open('C:\\Users\\joaob\\OneDrive\\Documentos\\BarbeariaFinal\\horariosIndisponiveis.txt', 'r', encoding="utf-8" , errors="ignore") as ler:
        visualizar = ler.readlines()
        if visualizar:
            print()
            for linha in visualizar:
                print(linha.strip())  # remove as quebras de linha ao imprimir
            #Nesse código, verificamos se visualizar (o conteúdo do arquivo) não está vazio. 
            # Se não estiver vazio, imprimimos o conteúdo linha a linha, removendo as quebras de linha. 
            # Se estiver vazio, informamos que nenhum horário indisponível foi encontrado. 
            # Isso evitará a impressão dos colchetes "[]" quando o arquivo estiver vazio.
            # A quebra de linha também esta possibilitando que as mensagens não apareçam dentro de colchetes
            #Isso deve resultar em uma saída mais legível, sem os colchetes 
            # Os colchetes aparecem por que visualizar acaba virando uma lista com varios valores adicionados
        else:
            print('Nenhum horário indisponível encontrado.')

def register(usuario, senha):
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f'{usuario}:{senha}\n')  #salvar os dados separando por :
# Função de login
def login(usuario, senha):
    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    # Verifica se as credenciais correspondem a algum usuário
    for linha in linhas: #Isso inicia um loop que percorre cada linha no arquivo.
        partes = linha.strip().split(":")  #atraves do strip e slip ele vai ler linha por linha / split(:) significa que ele vai ler o que ta antes e depos do :
        if len(partes) == 2:               #verifica se a linha foi dividida corretamente em duas partes, ou seja, se contém tanto um "nome" quanto uma "senha"
            nome, senha_salva = partes 
            if nome == usuario and senha_salva == senha:
                print()
                return servico
#Com essa abordagem, você terá os dados de cada usuário organizados e será mais fácil ler e verificar as credenciais durante o login. Certifique-se de adaptar outras partes do código conforme necessário para trabalhar com essa nova estrutura de dados.

def visualizarCliente(nome, senha):
    with open('user.txt', 'r', encoding="utf-8" , errors="ignore") as arquivo:
        visualizar = arquivo.readlines()
        if (nome == 'Joao Alberto' or nome == 'Guilherme Alencar') and senha == '12345':
            if visualizar:
                print("\nHorários marcados: ")
                for linha in visualizar:
                    print(linha.strip())  # Isso remove as quebras de linha ao imprimir
            else:
                print()
                print('Nenhum horário marcado.')
        else:
            print()
            print('Apenas os barbeiros têm acesso.')
#função principal onde agenda o corte
def servico(nome, selecionar, barber1, barber2, escolha):
    princ = []
    #dicionaro que serviu para guardar o serviço escolhido pelo cliente e conseguir aparecer na mensagem final
    descricao_servicos = {
    1: 'Cabelo',
    2: 'Cabelo + sobrancelha',
    3: 'Cabelo + Barba',
    4: 'Cabelo + Sobrancelha + Barba',
    5: 'Sobrancelha',
    6: 'Barba',
    7: 'Barbaterapia + Corte',
    8: 'Platinar + Corte'
}
    if selecionar == 1:
        print(f'O cliente {nome} selecionou o serviço de {descricao_servicos.get(escolha, "Serviço não encontrado")} com o barbeiro {barber1}')
        with open("user.txt", "a") as arquivo1:
            arquivo1.write(f'{nome} - ') 
    if selecionar == 2:
        print(f'O cliente {nome} selecionou o serviço de {descricao_servicos.get(escolha, "Serviço não encontrado")} com o barbeiro: {barber2}.')
    else: 
        pass
    
#Função menu principal

def menu(opcao):
            if opcao == 1:
                return register
            if opcao == 2:
                return login
            if opcao == 3:
                return visualizarCliente
            if opcao == 4:
                print()
                print('Obrigado por entrar em contato conosco. Volte sempre!')
                print()
                sys.exit()