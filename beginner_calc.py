class Calculator :
    @staticmethod
    def greet():
        print(f'Good Morning... {a.name}')

    def __init__(self, n):
        self.n = n

    def calc_sq(self):
        print(f'The square of the number {self.n} is : {self.n**2}')

    def calc_cube(self):
        print(f'The cube of the number {self.n} is : {self.n**3}')

    def calc_sq_root(self):
        print(f'The square root of the number {self.n} is : {self.n**(1/2)}')


a = Calculator(16)

a.greet()
a.calc_sq()

a = Calculator(12)
a.calc_cube()

a = Calculator(625)
a.calc_sq_root()