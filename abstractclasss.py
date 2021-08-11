from abc import ABC,abstractmethod
class employee(ABC):
    _id=0
    def detail(self,name,age,_id):
        self.name=name
        self.age=age
        self._id=id
    def show(self):
        print(self.name,self.age,self._id)
e=employee()
e.detail('kartik', 20, 3)
e.show()
class data(employee):
    def show(self):
        print(self.name,self.age,self._id)
        
d=data()
d.detail('rahul', 22,1)
d.show()
d.detail('mohit', 21, 2)
d.show()

