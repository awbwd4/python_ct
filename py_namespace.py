class Stock:
    market = "kospi"

print(dir())



s1 = Stock()
s2 = Stock()
print(id(s1))
print(id(s2))

print(dir())

print(Stock.__dict__)
print(s1.__dict__)
print(s2.__dict__)

print(s1.market)


s1.market = "kosdaq"
print(s1.__dict__)
print(s1.market)
# s2.market = "kospi"
print(s2.market)
print(s2.__dict__)
