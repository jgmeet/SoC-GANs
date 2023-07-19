'''
class computer:   # class

    def __init__(self,cpu,ram):  # constructor
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config for", self, "is", self.cpu, self.ram)
        # print(self)


# let's create object of class computer
comp1 = computer('M1','8GB')
computer.config(comp1)
# computer.config(930904104)

# another method to call config, this is mostly used
comp2 = computer('i5','8GB')
# note that we are nit passing any argument, but ut will take camp2 as argument in backened
comp2.config()
'''

'''
class computer:
    def __init__(self) -> None:
        self.name = "mac m1"
        self.model = 2020

    def update_name(self):
        self.name = 'mac m2'

    def compare(self, other):
        return self.model == other.model


c1 = computer()
c2 = computer()
print("c1 model:", c1.model)
print("c2 model:", c2.model)

c1.model = 2021
# print("c1 model:", c1.model)
# print("c2 model:", c2.model)

if c2.compare(c1): print("same")
else: print("not same")


print("c1 name:",c1.name)
print("c2 name:",c2.name)

c2.update_name()
print("c1 name:",c1.name)
print("c2 name:",c2.name)
'''



# class variables and instance variables
'''
class car:

    # variables declared outside init are class varriables
    # changning them for one object will change for all objects
    wheels = 4

    def __init__(self) -> None:
        # variables declared here are instance variables and chagning for one object will not affect others
        self.com = 'Range-Rover'
        self.color = 'White'


car1 = car()
car2 = car()

car2.color = 'Black'
car.wheels = 5

print(car1.com, car1.color, car1.wheels)
print(car2.com, car2.color, car2.wheels)
'''



# class in class
'''
class student:

    def __init__(self,name,rollno,lapt):
        self.name = name
        self.rollno = rollno
        self.lap = lapt


    def show(self):
        print(self.name, self.rollno)
        self.lap.show()


    class laptop:
        def __init__(self):
            self.brand = 'mac'
            self.ram = 8
            self.rom = 256

        def show(self):
            print(self.brand,self.ram,self.rom)



lap1 = student.laptop()


s1 = student('shelt',35,lap1)
# print(s1.name) # or you can use method
s1.show()
'''


# inheritance in python
'''
class A:

    def __init__(self):
        print("in init of A")


    def feature1(self):
        print("feature1-A")

    def feature2(self):
        print("feature2")


class B(A):   # class B is child of class A

    def __init__(self):
        super().__init__() # ** will call init of A
        print("in init of B")

    def feature3(self):
        print("feature3")

    def feature4(self):
        print('feature4')


class D:
    def __init__(self) -> None:
        print("in init of D")

    def feature1(self):
        print('feature1-D')


# ** Method resolution order (MRO)
class E(A,D):    # for multiple inheritance, class E(A,D)

    def __init__(self):
        super().__init__() # by MRO, init will be called for 1st parent classes from left side
        print("in init of E")

    # calling methods of super/parent class
    def feat(self):
        super().feature2()


# a1 = A()
# a1.feature1()
# a1.feature2()

# b1 = B()
# b1.feature2()
# b1.feature3()

e1 = E()

# MRO applies for methods
e1.feature1()
e1.feat()
'''



# Polymorphism, one thing behaves in may forms

# Duck typing
'''
class Pycharm:

    def execute(self):
        print('compiling....')
        print('running....')


class MyEditor:

    def execute(self):
        print('compiling....')
        print('running....')
        print('executed ✅')
        print('output')

class laptop:

    def compile_code(self,ide):
        ide.execute()


ide = Pycharm()

# let's now change ide to MyEditor
ide = MyEditor()


lap = laptop()
lap.compile_code(ide)
'''



# Operator overloading
'''
class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        
        s = student(m1,m2)
        return s

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)


s1 = student(8,9)
s2 = student(10,8)

s3 = s1 + s2
print(s3.m1, s3.m2)

print(s1)
'''


# Method overloading

class student:

    def __init__(self) -> None:
        self.m1 = 10
        self.m2 = 20


    def sum(self, a, b, c=0):
        return a+b+c


s1 = student()
print(s1.sum(3,60))
print(s1.sum(1,10,9))