#ชื่อ,เงินเดือน
class Employee: #การสร้างcalss
    # สร้าง Method
    def detail(self, name,salary,department):
        # สร้าง Attribute
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))

#Attribute เป็นกลไกลที่กำหนดคูณสมบัติให้กับ class
#การสร้างAttribute
 # self.name = ชื่อพนักงาน
 # self.salary = เงินเดือน
 # self.age = อายุของพนักงาน
# Method เป็นกลไกที่กำหนดพฤติกรรมให้กับ class
# การสร้าง Method
#   def getName(self)
#       return self.name
# การเรียกใช้งาน
#   ชื่อวัตถ.getName()

# คีย์เวิร์ด self
#   การใช้คีย์เวิร์ด self จะเป็นตัวชี้หรือบ่งบอกว่าตอนนี้เราทำงานกับวัตถุใด
#   ให้บอกตัวตนของวีตถุนั้นๆ เช่น การกำหนดคุณสมบัติต่างๆในวัตถุ

# Constructor
# เป็น Method พิเศษที่จะถูกสร้างใช้งานเมื่อเริ่มสร้างวัตถุ (ไม่ระบุก็ได้)
#โครงสร้าง constructor
#   def __init__(self):
#การสร้างวัตถุ

emp1= Employee()
emp1.detail('Apinya', 200000,'Department Head')
emp1.showData()

emp2= Employee()
emp2.detail('Vincent',500000, 'Manager')
emp2.showData()

emp3= Employee()
emp3.detail('Roddy', 10000,'Employee')
emp3.showData()
