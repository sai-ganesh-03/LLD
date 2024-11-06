from Node import Node

class File(Node):
    def __init__(self,name):
        super().__init__(name)
        
    def ls(self):
        print("File: ",self.name)