from Node import Node

class Directory(Node):
    def __init__(self,name):
        super().__init__(name)
        self.nodes:list[Node]=[]
        
    def ls(self):
        print("Directory: ",self.name)
        for node in self.nodes:
            node.ls()
            
    def add_nodes(self,node:Node):
        self.nodes.append(node)