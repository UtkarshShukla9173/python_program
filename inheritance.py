class Polygon:
    def __init__(self,side):
        self.side=side
    def display(self):
        print('pyhton i snaty')
    def perimeter(self):
        result= sum(self.side)
        return result
class triangle(Polygon):
    def display(self):
        super().display()
        print("triangle has 3 side")
        
        
        

t1= triangle([5,6,7])
print(t1.perimeter())
t1.display()