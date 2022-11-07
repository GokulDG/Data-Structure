class NewNode():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        newnode = NewNode(value)
        if self.root is None:
            self.root = newnode
            print("first case executed!")
            return True
        temp = self.root
        while temp is not None:
            if temp.value == newnode.value:
                print("Same value is able to insert in Tree")
                return False
            if temp.value < newnode.value:
                if temp.right is None:
                    temp.right = newnode
                    print("Second case is executed!")
                    return True
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = newnode
                    print("third case is executed!")
                    return True
                temp = temp.left

    def contain(self, value):
        temp = self.root
        while temp is not None:
            if temp.value < value:
                temp = temp.right
            elif temp.value > value:
                temp = temp.left
            else:
                print("Value is there !")
                return True
        else:
            print("Value is not there !")
            return False

    def maximum(self):
        temp = self.root
        while temp.right is not None:
            temp = temp.right
        return temp.value

    def minimam(self):
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        return temp.value

binaryobj = BinaryTree()
print("=================  insert  ======================")
binaryobj.insert(10)
binaryobj.insert(50)
binaryobj.insert(60)
binaryobj.insert(40)
binaryobj.insert(70)
binaryobj.insert(30)
binaryobj.insert(100)
#print(binaryobj.root.value)
print("=================== contain ====================")
binaryobj.contain(80)
binaryobj.contain(50)
binaryobj.contain(40)
binaryobj.contain(100)
print("=================== Maximum ====================")
print(binaryobj.maximum())
print("=================== Minimam ====================")
print(binaryobj.minimam())
