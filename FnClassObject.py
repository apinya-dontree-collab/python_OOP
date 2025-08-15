#FnClassObject
# ฟังก์ชั่นที่ทำงานร่วมกับ class และ object

#isinstance และ dir คือฟังก์ชั่นที่ทำงานร่วมกับ class และ object
#โดยมีรายละเอียด ดังนี้
#isinstance=> เช็คว่า object นี้ถูกสร้างจาก class ที่เรานิยามหรือไม่
#dir => แสดง attribute และ method
# __class__ => แสดงชื่อ class และ object

class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))

        #มีหรือไม่มีก็ได้ destructor
        def __del__(self):
            print('call destructor')

emp1 = Employee('Apinya', 200000, 'Department Head')
emp2 = Employee('Vincent', 50000, 'Manager')
emp3 = Employee('Roddy', 10000, 'Employee')
emp4 = Employee('Yuta', 10000, 'HR')

print(isinstance(emp1, Employee)) # ตรวจสอบว่า Obj ถูกสร้างจาก class ที่ตรวจสอบไหม
print(dir(emp1))
print(emp1.__class__)