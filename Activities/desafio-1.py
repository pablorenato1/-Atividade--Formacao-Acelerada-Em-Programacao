# Ana precisa de um sistema para coordenar os membros(nome) da equipe e as tarefas (descricao) atribuídas a cada um deles.
# Neste sistema, cada membro da equipe pode ter várias tarefas atribuídas, mas uma tarefa específica está ligada apenas a um
# membro da equipe.
# Sugestão utilizar array e função.


class task:
    def __init__(self, description, taskId) -> None:
        self.description = description
        self.memberId = None
        self.taskId = taskId


class employee:
    def __init__(self, name, memberId) -> None:
        self.name = name
        self.memberId = memberId
        self.tasks = []

    def addTask(self, task) -> None:
        if task.memberId == None:
            self.tasks.append(task)
            task.memberId = self.memberId
        else: print("Task already assigned to someone.")

    def removeTask(self, task) -> None:
        if task in self.tasks:
            self.tasks.remove(task)



task1 = task("Clean the bathroom",1)
task2 = task("Code challenge.", 2)
task3 = task("Improve Notion Documentation", 3)

employee1 = employee("Pablo Renato",1)
employee2 = employee("Kaly Susu", 2)
employee3 = employee("VItor Marcos", 3)

employee1.addTask(task1)
employee1.addTask(task2)
employee2.addTask(task1)
employee3.addTask(task3)

print("Employee")
for temp in employee1.tasks:
    print(f"Employee1: {temp.memberId}")
for temp in employee2.tasks:
    print(f"Employee2: {temp.memberId}")
for temp in employee3.tasks:
    print(f"Employee3: {temp.memberId}")


print("Tasks")
print(task1.memberId)
print(task2.memberId)
print(task3.memberId)