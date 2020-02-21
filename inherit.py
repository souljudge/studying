#inherit 继承
class Father():
    def eat(self):
        print("father can eat")
class Mother():
    def walk(self):
        print("walk like mother")

class Son(Father,Mother):
    def eat(self):
        print("eat like father")
littlehu=Son()
littlehu.eat()