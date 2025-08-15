class Employee:
    def __init__(self, name, salary, department):

        self._name = name
        self._salary = salary
        self._department = department
        self._showData(self):

        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))

emp1 = Employee('Apinya', 50000, 'Department Head')
emp1.salary = 30000
