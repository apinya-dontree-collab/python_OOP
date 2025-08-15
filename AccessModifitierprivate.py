class Employee:
    def __init__(self, name, salary, department):
        # Private Attributes
        self.__name = name
        self.__salary = salary
        self.__department = department

    # Public Method สำหรับเข้าถึงข้อมูล Private
    def showData(self):
        print(f'ชื่อพนักงาน = {self.__name}')
        print(f'เงินเดือน = {self.__salary}')
        print(f'แผนก = {self.__department}')

    # Setter Method สำหรับเปลี่ยนค่า Private

    # Getter Method สำหรับอ่านค่า Private
    def getSalary(self):
        return self.__salary

emp1 = Employee('อาทิตย์', 50000, 'วิชาการ')
emp1.setSalary(51000) # เปลี่ยนค่า salary ผ่าน Setter Method
print(f'เงินเดือนใหม่ของ {emp1.getSalary()} บาท') # อ่านค่า salary ผ่าน Getter Method
emp1.showData() # เรียกใช้ Public Method แสดงข้อมูล
