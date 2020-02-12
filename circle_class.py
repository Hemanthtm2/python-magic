class Circle():
    
    pi=3.14
    
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius*radius*Circle.pi  #otherwise use self.pi
        
    def get_circumference(self):
        return self.radius*self.pi*2


c=Circle(30)

print(c.get_circumference())
print(c.area)

print(c.radius)
