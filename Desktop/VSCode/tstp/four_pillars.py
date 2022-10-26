
# class Data: 
#     def __init__(self) :
#         self.nums = [1, 2, 3, 4, 5]
        
#     def change (self, i, n):
#         self.nums[i] = n 

# data1 = Data()
# data1.nums[0] = 50
# print (data1.nums)

# data2 = Data()
# data2.change(0, 50)
# print(data2.nums)


## INHERITANCE


# class Shape():
#     def __init__(self, w, l):
#         self.width = w 
#         self.len = l


#     def print_size(self): 
#         print("""{} by {} """.format(self.width, self.len)) 
# #method print_size is used to pull the values of parameters in class Shape, 
# # and fill the blanks inside the string

# class Square(Shape) : 
#    ### pass
# # the class "Square" would be considered a child class as it is utilizing the methods from the class "Shape".
# #the "Square" class passes through "Shape" because it was used a its parameter, 
# # thus 'inhereting' its attributes suchs as variables and methods

# #you can also add new methods, called method overriding, to override the parent methods of the same name
#     def area(self) :
#         return self.width * self.len

#     def print_size(self): 
#         print("""I am {} by {} """.format(self.width, self.len)) 

# my_shape = Shape(20, 35)
# my_shape.print_size() 


#COMPOSITION

# class Dog():    #method for the dog, describing name, breed, owner
#     def __init__(self, name, breed, owner) :
#         self.name = name
#         self.breed = breed
#         self.owner = owner 


# class Person():    # method for the person, giving game
#     def __init__(self, name) :
#         self.name = name

# oh = Person("Oscar") # variable created to give value "Oscar" to Person
# pet = Dog("Chili", "Doxie", oh) # variable created to give value to Dog parameters

# print(pet.owner.name)

        
# class Rectangle():
#     def __init__(self, w, l) -> None:
#         self.width = w
#         self.len = l
    
#     def calculate_perimeter(self) :
#         return self.width *2 + self.len *2


# class Square():
#     def __init__(self, s1) -> None:
#         self.s1 = s1 
        

#     def calculate_perimeter(self) :
#         return self.s1 *4

# square = Square(5)
# print(square.calculate_perimeter(
# ))
# rect = Rectangle(10,5)
# print(rect.calculate_perimeter())

        

# class Square():
#     def __init__(self, s1) -> None:
#         self.s1 = s1 
        

#     def calculate_perimeter(self) :
#         return self.s1 *4
        
#     def change_size(self, new_side) :
#         self.s1 += new_side

# square = Square(25)
# print(square.s1)

# square.change_size(50)
# print(square.s1)


# class Shape():
#     def __init__(self, w, l) -> None:
#         self.width = w
#         self.len = l

#     def what_i_am(self) :
#         print("I am a shape")

# class Square(Shape) :
#     def __init__(self, s1) -> None:
#         self.s1 = s1 
        

#     def calculate_perimeter(self) :
#         return self.s1 *4
    
# class Rectangle(Shape) :
#     def __init__(self, w, l) -> None:
#         self.width = w
#         self.len = l
    
#     def calculate_perimeter(self) :
#         return self.width *2 + self.len *2


# rect = Rectangle(15,3)
# square = Square (15)

# rect.what_i_am(
# )
# square.what_i_am()

# print (rect.calculate_perimeter())
# print(square.calculate_perimeter())







# class Horse() :
#     def __init__(self, rider, name) -> None:
#         self.rider = rider
#         self.name = name

# class Rider() :
#     def __init__(self, name) -> None:
#         self.name = name
        
        
# rider1 = Rider("Chuck")
# horse = Horse(rider1, "Kuako")

# print("the name of the horse is {}".format(horse.name))
# print("The name of the rider is {}".format(rider1.name))
    

# class Father():
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
        
        

# class Mother() :
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

# class Son(): 
#     def __init__(self, name, age, parent1, parent2) -> None:
#         self.name = name
#         self.age = age
#         self.parent = parent1
#         self.par = parent2

# dad = Father('Lalo', 57)
# mom = Mother('Patty', 56)
# son1 = Son('Oscar', 29, mom, dad)
        
# print("Hi, my name is {}, I am {} years old. {} is my mother and {} is my father ".format(son1.name, son1.age, mom.name, dad.name))
# print("She is {} years old".format(mom.age))      
# print("He is {} years old".format(dad.age))
