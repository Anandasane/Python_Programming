# ================================================================
# 12 HYBRID INHERITANCE PATTERNS IN PYTHON
# Each example combines different types of inheritance
# ================================================================

print('========================================================== single + multiple ========================================================')

class Vehicle:
    def move(self):
        print("Vehicle moving")

class Car(Vehicle):          # Single inheritance
    def drive(self):
        print("Car driving")

class ElectricSystem:
    def charge(self):
        print("Charging battery")

class ElectricCar(Car, ElectricSystem):   # Multiple inheritance (Car + ElectricSystem)
    pass

print(ElectricCar.__mro__)   # Shows the order Python follows
e = ElectricCar()
e.move()
e.drive()
e.charge()
print('\n')


print('========================================================== single + multilevel ========================================================')

class Device:
    def start(self):
        print("Device starting")

class Computer(Device):      # Single
    def compute(self):
        print("Computing")

class Laptop(Computer):      # Multilevel (Device -> Computer -> Laptop)
    def portable(self):
        print("Portable")

class TabletOS:
    def touch(self):
        print("Touch interface")

class HybridLaptop(Laptop, TabletOS):   # Multiple + Multilevel
    pass

print(HybridLaptop.__mro__)
h = HybridLaptop()
h.start()
h.compute()
h.portable()
h.touch()
print('\n')


print('========================================================== single + hierarchical ========================================================')

class Animal:
    def breathe(self):
        print("Breathing")

class Mammal(Animal):        # Single
    def feed_milk(self):
        print("Feeding milk")

class Bird(Animal):          # Hierarchical sibling (Animal -> Bird)
    def fly(self):
        print("Flying")

class Dog(Mammal):           # Single, but sibling Bird exists => S + H
    def bark(self):
        print("Barking")

print(Dog.__mro__)
d = Dog()
d.breathe()
d.feed_milk()
d.bark()
print('\n')


print('========================================================== multiple + multilevel (Diamond) ========================================================')

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()      # Calls A's show

class C(A):
    def show(self):
        print("C")
        super().show()      # Calls A's show

class D(B, C):
    def show(self):
        print("D")
        super().show()      # Calls B.show -> C.show -> A.show

print(D.__mro__)
d_obj = D()
d_obj.show()
print('\n')


print('========================================================== multiple + hierarchical ========================================================')

class Person:
    def name(self):
        print("John")

class Employee:
    def salary(self):
        print("Salary: 50000")

class Developer(Person):     # Hierarchical branch 1
    def code(self):
        print("Coding")

class Manager(Employee):     # Hierarchical branch 2
    def manage(self):
        print("Managing")

class TechLead(Developer, Manager):   # Multiple inheritance
    pass

print(TechLead.__mro__)
tl = TechLead()
tl.name()
tl.code()
tl.salary()
tl.manage()
print('\n')


print('========================================================== multilevel + hierarchical ========================================================')

class Appliance:
    def power(self):
        print("Powered on")

class KitchenApp(Appliance):   # Multilevel
    def cook(self):
        print("Cooking")

class Oven(KitchenApp):        # Multilevel continues
    def bake(self):
        print("Baking")

class SmartDevice(Appliance):  # Hierarchical sibling
    def connect(self):
        print("WiFi Connected")

class SmartOven(Oven, SmartDevice):   # Multiple + Multilevel + Hierarchical
    pass

print(SmartOven.__mro__)
so = SmartOven()
so.power()
so.cook()
so.bake()
so.connect()
print('\n')


print('========================================================== single + multiple + multilevel ========================================================')

class Engine:
    def start(self):
        print("Engine start")

class CombustionEngine(Engine):   # Single
    def fuel(self):
        print("Fuel injected")

class ElectricMotor:
    def power(self):
        print("Motor powered")

class HybridControl:
    def balance(self):
        print("Balancing power")

class HybridEngine(CombustionEngine, ElectricMotor, HybridControl):   # Multiple + Multilevel
    pass

print(HybridEngine.__mro__)
he = HybridEngine()
he.start()
he.fuel()
he.power()
he.balance()
print('\n')


print('========================================================== single + multiple + hierarchical ========================================================')

class File:
    def read(self):
        print("Reading file")

class TextFile(File):          # Single
    def edit(self):
        print("Editing text")

class BinaryFile(File):        # Hierarchical sibling
    def execute(self):
        print("Executing binary")

class WordDoc(TextFile):       # Single (from TextFile)
    def format(self):
        print("Formatting word")

class EncryptedDoc(BinaryFile, WordDoc):   # Multiple + Hierarchical
    def decrypt(self):
        print("Decrypting")

print(EncryptedDoc.__mro__)
ed = EncryptedDoc()
ed.read()
ed.execute()
ed.edit()
ed.format()
ed.decrypt()
print('\n')


print('========================================================== single + multilevel + hierarchical ========================================================')

class Media:
    def play(self):
        print("Playing media")

class Audio(Media):            # Single
    def sound(self):
        print("Playing sound")

class MP3(Audio):              # Multilevel (Media -> Audio -> MP3)
    def mp3_codec(self):
        print("MP3 encoding")

class Video(Media):            # Hierarchical sibling
    def screen(self):
        print("Showing video")

class MP4(MP3, Video):         # Multiple + Multilevel + Hierarchical
    def mp4_codec(self):
        print("MP4 encoding")

class HD_MP4(MP4):             # Multilevel extension
    def hd_quality(self):
        print("1080p quality")

print(HD_MP4.__mro__)
hmp4 = HD_MP4()
hmp4.play()
hmp4.sound()
hmp4.mp3_codec()
hmp4.screen()
hmp4.mp4_codec()
hmp4.hd_quality()
print('\n')


print('========================================================== multiple + multilevel + hierarchical ========================================================')

class Person:
    def name(self):
        print("Name")

class Employee:
    def id(self):
        print("ID")

class Manager(Person):         # Hierarchical branch 1
    def manage(self):
        print("Managing")

class Engineer(Person):        # Hierarchical branch 2
    def code(self):
        print("Coding")

class Lead(Employee, Manager): # Multiple inheritance
    def lead(self):
        print("Leading")

class ProjectLead(Lead, Engineer):   # Multiple + Multilevel (Lead -> Employee) + Hierarchical
    def project(self):
        print("Managing project")

print(ProjectLead.__mro__)
pl = ProjectLead()
pl.name()
pl.id()
pl.manage()
pl.code()
pl.lead()
pl.project()
print('\n')


print('========================================================== single + multiple + multilevel + hierarchical ========================================================')

class A:
    def a(self):
        print("A")

class B(A):          # Single
    def b(self):
        print("B")

class C:             # Independent
    def c(self):
        print("C")

class D:             # Independent (sibling of C)
    def d(self):
        print("D")

class E(B, C, D):    # Multiple (B, C, D)
    def e(self):
        print("E")

class F(E):          # Multilevel (F -> E)
    def f(self):
        print("F")

print(F.__mro__)
f = F()
f.a()
f.b()
f.c()
f.d()
f.e()
f.f()
print('\n')


print('========================================================== complex MRO (duplicate ancestor) ========================================================')

class A:
    def identity(self):
        print("A")

class B:
    def identity(self):
        print("B")

class C(A):
    pass

class D(B):
    pass

class E(A):
    pass

class F(C, D, E):
    pass

print(F.__mro__)
f12 = F()
f12.identity()   # Calls A because A appears before B in the MRO
print('\n')

print('==================== All 12 hybrid inheritance patterns executed ====================')