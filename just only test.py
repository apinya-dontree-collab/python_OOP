class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def aging(self, year):
        print(f"อายุปัจจุบันของ {self.name}: {self.age} ปี")
        self.age += year
        print(f"อายุของ {self.name} หลังผ่านไป {year} ปี: {self.age} ปี")

# ตัวอย่างการใช้งาน
person = Human("สมชาย", 25)
person.aging(5)