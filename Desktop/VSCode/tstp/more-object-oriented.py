


# class Square(): #class Square is created
#     sqr = []  #creating list

#     # def __init__(self, s1, s2, s3, s4) -> None:
#         # self.s1 = s1
#         # self.s2 = s2                  #this def is the same as the following one except
#         # self.s3 = s3                  #its the long way. 
#         # self.s4 = s4
#         # self.sqr.append(self.s1)
#         # self.sqr.append(self.s2)
#         # self.sqr.append(self.s3)
#         # self.sqr.append(self.s4)

#     def __init__(self,side) -> None:
#         self.side = side
#         self.sqr.append(self.side)
        
#     def print_sides(self):
#         print("""{} by {} by {} by {}""".format(self.side, self.side, self.side, self.side))
#                                             #you can use the value fo the def multuple times inside
# s1 = Square(5)
# s2 = Square(10)
# # s3 = Square(25)
 

# # print(Square.sqr)
# s2.print_sides()

# a_square = Square(29)
# print(Square.sqr)
# another_square = Square(93)
# print(Square.sqr)


# oh = "Oscar"
# if oh is "Oscar":
#     print ("Yup")
# else:
#     print("Nope")

# class Person:
#     def __init__(self) -> None:
#         self.name = "Oscar"
        
# oh = Person()
# same_oh = oh
# print(oh is same_oh)

# other_oh = Person()
# print (other_oh is same_oh)

def compare(one1, one2):
    return one1 is one2 

print(compare("a","b"))
print(compare(1,1))
