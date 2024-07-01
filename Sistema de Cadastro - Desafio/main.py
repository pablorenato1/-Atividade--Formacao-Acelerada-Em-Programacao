# from .classes.member import member
from task import Task
from bancoDeDados import BancoDeDados

def main():
    banco = BancoDeDados()
    if not banco.connectToDatabase():
        return print("Erro ao estabelecer conexão com o banco.")

    while True:
        print('\nOpções:')
        print('1 - Listar Tasks')
        print('2 - Listar Employees')
        print('3 - Criar Employee')
        print('4 - Criar Task')
        print('5 - Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            tasks = Task()
            tasks.listOfAllTasks(banco)
        elif opcao == '2':
            banco.getAllEmployees()
            pass
        elif opcao == '3':
            nome = input('Digite o nome do novo Employee: ')
            supervisorId = input('Digite o ID do supervisor (ou deixe em branco se não houver): ')
            banco.addObjetcToEmployee(nome)
        elif opcao == '4':
            memberId = input('Digite o ID do Employee para atribuir a Task: ')
            dateOfCreation = input('Digite a data de criação (AAAA-MM-DD): ')
            dateToEnd = input('Digite a data de término (AAAA-MM-DD): ')
            description = input('Digite a descrição da Task: ')
            # criar_task(conn, memberId, dateOfCreation, dateToEnd, description)
            banco.addObjetcToTask(description)
        elif opcao == '5':
            break
        # else:
        #     print('Opção inválida. Por favor, escolha uma opção válida.')

    print('Programa encerrado.')

if __name__ == '__main__':
    main()