# 面向对象 object oriented
# class Student():
#     def eat(self):
#         print("student can eat")
#     def study(self):
#         print("student can study")
#
# Student().eat()
# Student().study()

# class Student():
#     def eat(self, name,age):
#         print(name + " can eat"+" and his/her age is "+age)
#
#     def study(self):
#         print("student can study")
#
#
# Student().eat('cuihuxun','22')

class Student():
    name='cuihuxun'
    age='18'
    def eat(self):
        print(self.name,"can eat"+" and his age is",self.age)
    @staticmethod
    #一旦使用@staticmethod,就不能调用class中的variable
    def walk():
        print("student can walk")

Student().eat()
Student().walk()
