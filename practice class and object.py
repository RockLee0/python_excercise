
class Employee:
    def __init__(self, a, b):
        self.id = a
        self.name = b


emp = Employee(1, "coder")

print(emp.name)

del emp.id
print(emp.id)

del emp

print(emp)