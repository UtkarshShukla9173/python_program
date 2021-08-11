from os import path



def createfile(dest):
    if not (path.isfile(dest)):
        f=open(dest,'w')
        f.write('welcome to python scripting')
        f.close()
        f.read(dest)


dest="C:\\Users\\shukl\\.spyder-py3\\sample.txt"

createfile(dest)

print("File created")