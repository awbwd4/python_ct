class BusinessCard :
    def set_inf(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr


member1 = BusinessCard()
member1
member1.set_inf(name, email, addr)


class BusinessCard:
    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
    def print_info(self):
        print("-----------------------")
        print("name: ", self.name)
        print("e mail : ", self.email)
        print("address : ", self)


