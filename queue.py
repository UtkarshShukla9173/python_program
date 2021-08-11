class stack:
    def __init__(self):
        self.my_stack=[]
    def push(self,value):
       return  self.my_stack.append(value)
    def is_empty(self):
        self.my_stack=[]
    def pop(self):
        if (self.my_stack)==([]):
            print("stack is empty")
            
        
        else:
            self.my_stack.pop(0)
        return self.my_stack
    def display(self):
        return self.my_stack
    def one(self):
        t=int(input("how many values u want to push in queue"))
        for i in range(t):
            value=int(input("enter value to be pushed in stack"))
            s.push(value)
    def two(self):
        #value=int(input("enter value to be pushed in stack"))
        print(s.pop())
    def three(self):
    #    value=int(input("enter value to be pushed in stack"))
        print(s.display())

    def case(self,v):
        
        if v==1:
            s.one()
        elif v==2:
            s.two()
        elif v==3:
            s.three()
        
        
s=stack()
while(True):
    v=int(input('''1 to push\n2 to pop\n3 to display\n4. to exit  ='''))
    s.case(v)
   
    if v==4:
       break 
    '''else:
        s.case()'''
