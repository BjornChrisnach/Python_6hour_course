# import inspect

# print(inspect.getsource(list))
# x = [1, 2, 3]
# y = [4, 5]

# print(type(x))

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name})"

    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument, must be int")

        self.name = self.name * x

    def __call__(self, y):
        print("called the is function", y)

    def __len__(self):
        return len(self.name)


p = Person("Tim")
print(len(p))
