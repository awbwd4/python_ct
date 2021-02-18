class Parent:
    def can_sing(self):
        print("Sing a song")


father = Parent()
father.can_sing()

class LuckyChild(Parent):
    pass

child1 = LuckyChild()
child1.can_sing()


class UnluckyChild():
    pass

child2 = UnluckyChild()
# child2.can

class LuckyChild2(Parent):
    def can_dance(self):
        print("Shuffle Dance")


child2 = LuckyChild2()

print("==========================")
child2.can_sing()
child2.can_dance()






# C:\Users\JaeukKo\Desktop\trading_algorithm
