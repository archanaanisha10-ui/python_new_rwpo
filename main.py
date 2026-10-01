class myclass:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        return f"The multiplication is {self.x} * {other.x} = " + str(self.x * other.x)


obj1 = myclass(10)
obj2 = myclass(30)

print(obj1 * obj2)


obj3 = myclass(100)
obj4 = myclass(500)

print(obj3 * obj4)
