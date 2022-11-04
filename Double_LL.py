class NewNode():
    def __init__(self,value):
        self.value = value
        self.pre = None
        self.next = None

class DoubleLindedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            while temp != None:
                print(temp.value)
                temp = temp.next

    def append(self, value):
        newnode = NewNode(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
            self.length += 1
        else:
            self.tail.next = newnode
            newnode.pre = self.tail
            self.tail = newnode
            self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        else:
            if self.length == 1:
                self.head = None
                self.tail = None
                self.length -= 1
                return None
            temp = self.tail
            self.tail = temp.pre
            self.tail.next = None
            temp.pre = None
            self.length -= 1

    def prepand(self, value):
        newnode = NewNode(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
            self.length += 1
        else:
            self.head.pre = newnode
            newnode.next = self.head
            self.head = newnode
            self.length += 1

    def popfirst(self):
        if self.length == 0:
            return None
        else:
            if self.length == 1:
                self.head = None
                self.tail = None
                self.length -= 1
                return None
            temp = self.head
            self.head = self.head.next
            self.head.pre = None
            temp.next = None
            self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index < self.length // 2:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp       #.value  for get()
        else:
            temp = self.tail
            for i in range(self.length-1, index, -1):
                temp = temp.pre
            return temp       #.value  for get()

    def set(self, value, index):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, value, index):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            self.prepand(value)
        elif index == self.length:
            self.append(value)
        else:
            newnode = NewNode(value)
            node = self.get(index)
            node.pre.next = newnode
            newnode.next = node
            newnode.pre = node.pre
            node.pre = newnode
            self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            self.popfirst()
        elif index == self.length -1 :
            self.pop()
        else:
            node = self.get(index)
            node.next.pre = node.pre
            node.pre.next = node.next
            self.length -= 1

doubleobj = DoubleLindedList()
print("============================ append ==============================")
for i in range(8):
    doubleobj.append(int(input("Enter the number to Append : ")))
print("length of the list: ",doubleobj.length)
doubleobj.print()

print("============================ pop ==============================")
for i in range(4):
    doubleobj.pop()
    print("length of the list: ",doubleobj.length)
doubleobj.print()

print("============================ popfirst ==============================")
print("length of the list: ",doubleobj.length)
for i in range(4):
    doubleobj.popfirst()
    print("length of the list: ",doubleobj.length)

print("============================ prepand ==============================")
for i in range(6):
    doubleobj.prepand(int(input("Enter the number to Prepand: ")))
doubleobj.print()
print("head of the list: ", doubleobj.head.value)
print("tail of the list: ", doubleobj.tail.value)

print("============================ get ==============================")
print("length of the list: ",doubleobj.length)
for i in range(4):
    print(doubleobj.get(int(input("Enter the index: "))))

print("============================ set ==============================")
doubleobj.set(100, 0)
doubleobj.print()

print("============================ insert ==============================")
doubleobj.insert(1000, 6)
doubleobj.print()
print("length of the list: ",doubleobj.length)

print("============================ remove ==============================")
for i in range(4):
    doubleobj.remove(int(input("Enter the index to Remove: ")))
doubleobj.print()
print("length of the list: ",doubleobj.length)
