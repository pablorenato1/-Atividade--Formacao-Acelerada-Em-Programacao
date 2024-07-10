from bancoDeDados import BancoDeDados
from task import Task

class SistemaPrincipal:
    def __init__(self) -> None:
        self.banco = BancoDeDados()
        self.task = Task()

    def menuUser(self):
        print('\nOpções:')
        print('1 - Lista de Tarefas')
        print('2 - Lista de Empregados')
        print('3 - Adicionar um novo Empregado')
        print('4 - Criar Tarefa')
        print('5 - Excluir Tarefa')
        print('6 - Alterar Tarefa')
        print('0 - Sair')

        option = input('Escolha uma opção: ')

        match option:
            case '1': # Show All Task
                self.showAllTask()
            case '2': # Show All Employee
                self.showAllEmployee()
            case '3': # Add new Employee
                self.addNewEmployee()
            case '4': # Add new Task
                self.registerNewTask()
            case '5': # Delete Task
                pass
            case '6': # Alter Task
                pass
            case '0': # Exit
                return self.endSystem()
            case _:
                print(f"Error: opção '{option}' é inválida ")
        
        return True
    
    def showAllTask(self):
        self.task.listOfAllTasks(self.banco)

    def showAllEmployee(self):
        self.banco.getAllEmployees()

    def registerNewTask(self):
        memberId = input('Digite o ID do Employee para atribuir a Task: ')
        dateOfCreation = input('Digite a data de criação (AAAA-MM-DD): ')
        dateToEnd = input('Digite a data de término (AAAA-MM-DD): ')
        description = input('Digite a descrição da Task: ')
        # criar_task(conn, memberId, dateOfCreation, dateToEnd, description)
        self.banco.addObjetcToTask(description)
    
    def alterTask(self):
        pass
    
    def deleteTask(self):
        pass
    
    def endSystem(self):
        return False

    def addNewEmployee(self):
        name = input('Digite o nome do novo Employee: ')
        supervisorId = input('Digite o ID do supervisor (ou deixe em branco se não houver): ')
        self.banco.addObjetcToEmployee(name)

    def deleteEmployee(self, id):
        pass