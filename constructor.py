#constructor
    #เป็น Method พิเศษที่จะถูกใช้งานเมื่อเริ่มสร่างวัตถุ (ไม่ระบุก็ได้)
    #โครงสร้าง constructor
        #def __init__(self):
        #   pass

        # destructor
        #เป็น method พิเศษที่ตรงข้ามกับ constructor จะถูกใช้งานเมื่อ
        #สิ้นสุดการทำงานของ Class หรือถูกทำก่อนจะสลาย object
        #ส่วนใหญ่จะเป็นกลุ่มคำสั่งที่ทำหน้าที่คืนหน่วยความจำให้ระบบ (ไม่ระบุก็ได้)
        #โครงสร้าง
        #def __del__(self):
        # pass

        # การสร้าง Constructor

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
emp1.showData()

emp2 = Employee('Vincent', 50000, 'Manager')
emp2.showData()

emp3 = Employee('Roddy', 10000, 'Employee')
emp3.showData()

emp4 = Employee('Yuta', 10000, 'HR')
emp4.salary = 30000
emp4.showData()