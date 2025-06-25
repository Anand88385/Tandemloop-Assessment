class Calculator:
    def __init__(self, a, b, op):
        self.a = a     
        self.b = b      
        self.op = op    

    def calc(self):
        if self.op == "add":
            return self.a +self.b
        if self.op == "sub":
            return self.a -self.b
        if self.op == "mul":
            return self.a *self.b
        if self.op == "div":
            
            if self.b == 0:
                return "cannot divide by 0"
            return self.a / self.b
        return "bad output"
a = int(input("a: "))
b = int(input("b: "))
op = input("op (add / sub / mul / div): ")

c = Calculator(a,b, op)
print(c.calc())
