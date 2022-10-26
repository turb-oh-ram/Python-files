# import math

# class Orange: #creates class. Syntax is in CamelCase
#     def __init__(self, w, c) : #creates method, which are defined in classes. 
#             #(instance variables = variables that define the class called.)
#             #(always use self as the first parameter of your method)
#         self.weight = w # defines the instance varibles 
#         self.color = c # ""

#         print('Created!')

# or1 = Orange(14, "light orange") #new object that gives value to the variables. 
# print (or1.weight)
# print(or1.color)


# ## find area of a rectangle

# class Rectangle():

#     def __init__(self, w, l) :
#         self.width = w 
#         self.len = l
#         print('created')

#     def area (self) : # method to find the area using the variables created.
#         return self.width * self.len

#     def change_size(self, w, l) : #new method created that allows me to input new values
#         self.width = w 
#         self.len = l

# rectangle = Rectangle(10,20)
# print (rectangle.area())
# rectangle.change_size(300, 500) ## using new method with new variables\
# print (rectangle.area())


# class Apple: 
#     def __init__(self, w, c, s, t) :
#         self.weight = w
#         self.color = c
#         self.size = s
#         self.type = t

# apple1 = Apple(8, "red", "medium", "Fuji")
# print (apple1.weight)
# print (apple1.color)
# print (apple1.size)
# print (apple1.type)


# class Circle() :
#     def __init__(self, radius):
#         self.radius = radius
       
#     def area(self) :
#         return self.radius **2 * math.pi

# a_circle = Circle(6)
# print(a_circle.area())


# class Triangle():
#     def __init__(self, b, h) :
#         self.base = b
#         self.height = h

#     def area(self) :
#         return self.base * self.height / 2

# triangle = Triangle (8,10)
# print(triangle.area())




class Hexagon ():
    def __init__(self, s1, s2, s3, s4, s5, s6) :
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def area(self) :
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

hex = Hexagon(3,3,5,5,2,2)
print(hex.area(

))
