#Super
#เม่อต้องการเรียกใช้งานคุณสมบัติต่างๆ ในคลาสแม่
#เช่น Constructor, Method,Attribute

#super().__init__(name)

class Employee:
    #class verible
    minsalary = 12000
    maxsalary = 50000
    companyName = 'บรึษัท ADJ จำกัด'
    def __init__(self, name, salary, department):
        # private attribute
        self.__name = name
        self.__salary = salary
        self.__department = department


    def _showData(self):
        print('ชื่อพนักงาน = '+self.__name)
        print('เงินเดือน = '+str(self.__salary))
        print('แผนก = '+self.__department)

class Accounting(Employee):
    __departmentName = 'แผนกพบัญชี'
    def __init__(self,name,salary):
        super().__init__(name,salary, self.__departmentName)
        super()._showData()


class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'
    def __init__(self,name,salary):
        super().__init__(name, salary,self.__departmentName)
        super()._showData()


class Sale(Employee):
    __departmentName = 'แผนกการขาย'
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()


account = Accounting("เกม",40000)
progerammr = Programmer("ปัท" ,17000)
sale = Sale("จิ๊บ",25000)

