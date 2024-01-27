class Parent:
    a=10
    b=20
    def __init__(self,c,d):
        self.c=c
        self.d=d
class Child(Parent):
  pass
obj=Child(4,5)