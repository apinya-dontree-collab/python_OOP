#เขียนโปรแกรมสร้าง class Tree โดu0 attribute และ metho ดังนี้
# attribute
#height เป็นความสูงต้นไม้
#width เป็นกว้างต้นไป
#generated_money เป็นเงินที่หาใต้
# method
#feed_A() ท่าหน้าที่แสดงด่าเงินที่หาใต้ และความกว่างของต้นไม้หลังจากให้ปียชนิด A
#โดยจะลด generated_money 10 หน่วย แต่จะเพิ่ม wigth 12 หน่วย
#feed_8() ท่าหน้าที่แสดงด่าเงินที่หาใด และความสูงของต้นไม่หลังจากให้ปียชนิด B
#โดยจะลด generated_money 8 หน่วย แต่จะเพิ่ม height 10 หน่วย
#sell() ท่าหน้าที่แสดงตาจ่านวนเงินที่นายต้นไม่ใต้ โดย generated_money จะเพิ่มเท่ากับ
#width * height * 0.8

class Tree:
    def __init__(self, height, width, generated_money):
        self.height = height
        self.width = width
        self.generated_money = generated_money

    def feed_A(self):
        self.generated_money = self.generated_money - 10
        self.width = self.width + 12

    def feed_B(self):
        self.generated_money = self.generated_money - 8
        self.height = self.height + 10


    def sell(self):
        self.generated_money = self.generated_money + self.width * self.height ** 0.8
        print('Width =', self.width, 'Heigth =', self.height )
        print('Generated_money =' , self.generated_money)

tree_A = Tree(10, 10, 1000)
tree_A.feed_A()
tree_A.feed_B()
tree_A.sell()

tree_B = Tree(23,8,254)
tree_A.feed_B()
tree_A.sell()

tree_c = Tree(300,14,580)
tree_A.feed_A()
tree_A.sell()