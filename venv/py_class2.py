class Foo:
    def func1():
        print("func1")
    def func2(self):
        print(id(self))
        print("func2")


f = Foo()
print(id(f))