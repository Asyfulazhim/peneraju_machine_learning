# class fruits:
#     def __init__(self, price):
#         self.price = price
# obj=fruits(50)
# obj.quantity=10
# obj.bags=2
# print(obj.quantity+len(obj.__dict__))

class Demo:
    def __init__(self):
        self.a = 1
        self.__b = 1
    def get(self):
        return self.__b
obj = Demo()
print(obj.get())