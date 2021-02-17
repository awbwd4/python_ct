class BusinessCard:
    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
    def print_info(self):
        print("name : ",self.name)
        print("email : ", self.email)
        print("addr : ", self.addr)

member1 = BusinessCard()

member1

member1.set_info("aaa", "bbb","ccc")

# member1.print_info()

class MyClass:
    def __init__(self):
        print("객체 생성")

inst1 = MyClass()


class BusinessCard2:
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
    def print_info(self):
        print("name : ",self.name)
        print("email : ", self.email)
        print("addr : ", self.addr)


inst2 = BusinessCard2("aaa", "bbb","ccc")
inst2.print_info()