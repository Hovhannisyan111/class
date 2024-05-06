"""
This file is for w3 resource exercisses
Created by: Arman Hovahnnisyan
"""
#OOP
#1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter. 

#class Circle():
#    def __init__(self,r, p):
#        self.radius = r
#        self.pi = p
#
#    def area(self):
#        return self.pi * self.radius**2
#
#    def parimeter(self):
#        return 2 * (self.radius * self.pi)
#    
##    def __str__(self):
##        retrun f" "
#
#
#
#
#r = Circle(5, 3.14)
#print("Area: ", r.area())
#print("Parimmeter: ", r.parimeter())

#2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

#class Person():
#    def __init__(self, n, c, a):
#        self.name = n
#        self.country = c
#        self.age = a
#    
#    def __str__(self):
#        return f"Name-{self.name} Country-{self.country} Age-{2024 - self.age}"
#
#
#h1 = Person("Jack", "France", 1999)
#print(h1)

#3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations. 

#class Math():
#    def __init__(self, n):
#        self.num = n
#
#    def __add__(self, other):
#        return Math(self.num + other.num)
#    def __sub__(self, other):
#        return Math(self.num - other.num)
#    def __mul__(self, other):
#        return Math(self.num * other.num)
#    def __floordiv__(self, other):
#        return Math(self.num / other.num)
#
#    def __str__(self):
#        return f"{self.num}"
#
#num1 = Math(20)
#num2 = Math(5)
#print(num1+num2)
#print(num1-num2)
#print(num1*num2)
#print(num1//num2)
