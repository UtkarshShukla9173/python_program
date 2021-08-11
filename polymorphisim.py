class pycharm:
  def execute(self):
    print("compliling")
    print('running')

class Myeditor:
  def execute(self):
    print("spell check")
    print("convention check")
    print("running")
    print("compiling")

class Laptop:
  def code(self,ide):
    ide.execute()


ide = Myeditor()  #duck typing (same object can e use for different methons as it form same task everywhere.)

lap1 = Laptop()
lap1.code(ide)
