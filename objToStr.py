#objectToString

#แปลง Object เป็น String
#def __str__(self)
#   return "ชุดข้อความ"

class Employee:
    minSalary = 12000
    maxSalary = 50000
    companyName = 'บรึษัท ADJ จำกัด'

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department

    # แสดงรายละเอียด
    def showData(self):
        print('ชื่อพนักงาน = ' + self.__name)
        print('เงินเดือน = {}'.format(self.__salary))
        print('แผนก = ' + self.__department)

    # รายได้ต่อปี
    def getIncome(self):
        return self.__salary * 12

    def __str__(self):
        return "พนักงาน: {} แผนก: {} เงินเดือน: {} รายได้ต่อปี: {}".format(
            self.__name, self.__department, self.__salary, self.getIncome())


class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super().showData()


class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super().showData()


class Sale(Employee):
    __departmentName = 'แผนกขาย'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super().showData()

account = Accounting("เกม",40000)
print(account.__str__())
progerammr = Programmer("ปัท" ,170000)
print(progerammr.__str__())
sale = Sale("จิ๊บ",25000)
print(sale.__str__())
