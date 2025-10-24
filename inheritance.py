# Base class
class Vehicle:
    def start_engine(self):
        print("Engine started")

# Derived class
class Car(Vehicle):
    pass  # No method overriding

# Creating objects
v = Vehicle()
c = Car()

# Calling the method
v.start_engine()  # Output: Engine started
c.start_engine()  # Output: Engine started (inherited from Vehicle)
print("multiple inheritance")
class Father:
    def father_info(self):
        print("This is the Father class")

class Mother:
    def mother_info(self):
        print("This is the Mother class")

class Child(Father, Mother):
    def child_info(self):
        print("This is the Child class")

c = Child()
c.father_info()
c.mother_info()
c.child_info()
print("multi level inheritance")
class Grandparent:
    def show_gp(self):
        print("This is the Grandparent class")

class Parent(Grandparent):
    def show_p(self):
        print("This is the Parent class")

class Child(Parent):
    def show_c(self):
        print("This is the Child class")

c = Child()
c.show_gp()
c.show_p()
c.show_c()
print("Hierarchical Inheritance")
class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def dog_sound(self):
        print("Dog barks")

class Cat(Animal):
    def cat_sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
d.dog_sound()

c.sound()
c.cat_sound()
print("Hybrid Inheritance")
class A:
    def method_a(self):
        print("Method in class A")

class B(A):
    def method_b(self):
        print("Method in class B")

class C(A):
    def method_c(self):
        print("Method in class C")

class D(B, C):  # Inherits from both B and C
    def method_d(self):
        print("Method in class D")

d = D()
d.method_a()
d.method_b()
d.method_c()
d.method_d()


