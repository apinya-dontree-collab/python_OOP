#ClassInstanceVeriable

#Class Verible คือ ตัวแปรที่ทำงานภายใน Class
#ส่วนอื่นสามารถเข้าถึงข้อมูลส่วนนี้ได้เลย (static attribute)
#โดยไม่จำเป็นต้องสร้าง Object ขิ้นมา

#instance Veriable คือ ตัวแปรที่อยู่ภายใน object
#สามารถเข้าถึงข้อมูลส่วนนี้ได้โดยต้องสร้าง Object ขึ้นมา

class Employee:
    #class verible
    __minsalary = 12000
    __maxsalary = 50000
    _companyName = 'บรึษัท ADJ จำกัด'
    def __init__(self, name, salary, department):
        # private attribute
        self.__name = name
        self.__salary = salary
        self.__department = department


    def _showData(self):
        print('ชื่อพนักงาน = {}'+self.__name)
        print('เงินเดือน = {}'+self.__salary)
        print('แผนก = {}'+self.__department)


emp1 = Employee('อภิญญา', 50000, 'ผู้จัดการ')
#print('เงินเดือนขั้นต่ำ ='+str(Employee.__minsalary))
print(Employee._companyName)
