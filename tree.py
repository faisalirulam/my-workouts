class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=node(data)
    def show(self):
        if self.left:
            self.left.show()
        print(self.data)
        if self.right:
            self.right.show()


root=node(2)
root.insert(22)
root.insert(33)
root.show()

