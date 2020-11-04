
class Student:
    c=0
    a=0
    b=0
    def displayResult(self):
        self.c=self.a+self.b
        print("Sum", self.c)



s=Student()
s.a=10
s.b=20
s.displayResult()