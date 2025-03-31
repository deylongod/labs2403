class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    def get_info(self):
        return f'Имя: {self.name}, ID: {self.emp_id}'

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department
    def manage_project(self, project):
        return f'Менеджер {self.name} из отдела {self.department} управляет проектом: {project}'

class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization
    def perform_maintenance(self):
        return f'Техник {self.name} выполняет обслуживание в области: {self.specialization}'

class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Employee.__init__(self, name, emp_id)
        self.department = department
        self.specialization = specialization
        self.team = []
    def add_employee(self, employee):
        self.team.append(employee)
    def get_team_info(self):
        team_info = 'Команда:\n'
        for emp in self.team:
            team_info += f'- {emp.get_info()}\n'
        return team_info


emp = Employee("миша литвин", 666)
print(emp.get_info(), '\n')

mng = Manager("иван золочевский", 228, "киберспорт")
print(mng.manage_project("правильный геймплей на сфе, как попадать всеми койлами без скриптов"), '\n')

tec = Technician("эрик давидыч", 159, "не придумал")
print(tec.perform_maintenance(), '\n')

tech_manager = TechManager("дмитрий солдатов", 1487, "ритейл", "одежда и обувь")
print(tech_manager.manage_project("анализ и оптимизация бизнес-процессов"))
print(tech_manager.perform_maintenance(), '\n')
tech_manager.add_employee(emp)
tech_manager.add_employee(tec)
print(tech_manager.get_team_info())
