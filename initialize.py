class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def walk(self):
        print(self.name,'can walk')
        print(self.name,'is',self.age)

s1=Students('cuihuxun','18')
s1.walk()
s2=Students('xurui',22)
s2.walk()