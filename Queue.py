class NewNode():
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self,value):
        newnode = NewNode(value)
        self.first = newnode
        self.last = newnode
        self.length = 1

    def print(self):
        if self.length == 0:
            return None
        temp = self.first
        while temp != None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        newnode = NewNode(value)
        if self.length == 0:
            self.first = newnode
            self.last = newnode
            self.length += 1
        else:
            self.last.next = newnode
            self.last = newnode
            self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        else:
            temp = self.first
            self.first = temp.next
            temp.next = None
            self.length -= 1


queueobj = Queue(222)
print("length of the list : ", queueobj.length)
print("first of the list : ", queueobj.first.value)
print("last of the list : ", queueobj.last.value)
queueobj.enqueue(1)
queueobj.enqueue(2)
queueobj.enqueue(3)
queueobj.enqueue(5)
queueobj.enqueue(7)
queueobj.enqueue(8)
queueobj.enqueue(91)
queueobj.enqueue(10)
queueobj.print()
print("length of the list : ", queueobj.length)
print("first of the list : ", queueobj.first.value)
print("last of the list : ", queueobj.last.value)
queueobj.dequeue()
queueobj.dequeue()
queueobj.dequeue()
queueobj.dequeue()
queueobj.print()
print("length of the list : ", queueobj.length)
