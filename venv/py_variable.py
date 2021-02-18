class Account:
    num_account = 0

    def __init__(self, name):
        self.name = name
        Account.num_account += 1

    def __del__(self):
        Account.num_account -= 1

kim = Account("kim")
lee = Account("lee")

print(kim.name)
print(lee.name)

print(kim.num_account)
print(lee.num_account)

print(Account.num_account)