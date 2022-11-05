class NewNode():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.length = 0

    def print(self):
        if self.length == 0:
            return None
        temp = self.top
        while temp != None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        newnode = NewNode(value)
        if self.length == 0:
            self.top = newnode
            self.length += 1
        else:
            newnode.next = self.top
            self.top = newnode
            self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.length -= 1

stackobj = Stack()
print("======================== push  =================================")
stackobj.push(11)
stackobj.push(22)
stackobj.push(33)
stackobj.push(44)
stackobj.push(55)
stackobj.push(66)
print("Top of the list : ", stackobj.top.value)
stackobj.print()
print("======================== pop =================================")
stackobj.pop()
stackobj.pop()
stackobj.pop()
stackobj.pop()
stackobj.pop()
print("length of the list : ", stackobj.length)
stackobj.print()
