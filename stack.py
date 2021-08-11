class stack:
    def __init__(self):
        self.my_stack=[]
    def push(self,value):
        self.my_stack.append(value)
    def is_empty(self):
        self.my_stack=[]
    def pop(self):
        if (self.my_stack)==([]):
            print("stack is empty")
            
        
        else:
            self.my_stack.pop()
        return self.my_stack
    def display(self):
        print(self.my_stack)
    def one():
        value=int(input("enter value to be pushed in stack"))
        s.push(value)
    def two():
        #value=int(input("enter value to be pushed in stack"))
        print(s.pop())
    def three():
    #    value=int(input("enter value to be pushed in stack"))
        print(s.display())

    def case(v):
       
        switcher={
            1: s.one(),
            2: s.two(),
            3: s.three()
                }

s=stack()
s.case(1) 
 
