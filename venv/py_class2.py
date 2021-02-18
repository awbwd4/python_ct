class Foo:
    def func1():
        print("func1")
    def func2(self):
        print(id(self))
        print("func2")


f = Foo()
print(id(f))


# 13222720

f.func2()

Foo.func1()

# f.func1()


# Foo.func2()

f3 = Foo()

print(id(f3))

Foo.func2(f3)


# id(f3)