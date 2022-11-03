class NewNode():
    def __init__(self,value):
        self.value = value
        self.next = None

class SingleLinkedList():
    def __init__(self,value):
        newnode = NewNode(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1

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
            self.tail = newnode
            self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while temp.next != None:
            pre = temp
            temp = temp.next
        pre.next = None
        self.tail = pre
        self.length -= 1

    def prepand(self, value):
        newnode = NewNode(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
            self.length += 1
        else:
            newnode.next = self.head
            self.head = newnode
            self.length += 1

    def popfirst(self):
        if self.length == 0:
            return None
        else:
            temp = self.head.next
            self.head.next = None
            self.head = temp
            self.length -= 1

    def get(self, index):
        if index < 0 or self.length < index:    ##########
            return None
        #elif index == 0:
        #    return self.head.value
        #elif index == self.length - 1:
        #    return self.tail.value
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp  #.value  for get only

    def set(self, value, index):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, value, index):
        newnode = NewNode(value)
        if index < 0 or self.length < index:
            return None
        elif index == 0:
            self.prepand(value)
        elif index == self.length:
            self.append(value)
        else:
            temp = self.get(index-1)
            newnode.next = temp.next
            temp.next = newnode
            self.length += 1

    def remove(self, index):
        if index < 0 or self.length < index:
            return None
        elif index == 0:
            self.popfirst()
        elif index == self.length:
            self.pop()
        else:
            pre = self.get(index -1)
            node = self.get(index)
            pre.next = node.next
            node.next = None
            self.length -= 1




singleobj = SingleLinkedList(10)
print("========== append =================")
singleobj.append(20)
singleobj.append(40)
singleobj.append(60)
singleobj.append(80)
singleobj.print()
print("========== pop =================")
singleobj.pop()
singleobj.pop()
singleobj.pop()
singleobj.print()
print("========== prepend ================")
singleobj.prepand(66)
singleobj.prepand(77)
singleobj.prepand(88)
singleobj.prepand(99)
singleobj.prepand(100)
singleobj.prepand(110)
singleobj.print()
print("============ popfirst ===============")
singleobj.popfirst()
singleobj.popfirst()
singleobj.popfirst()
singleobj.print()
print("============ get ===============")
print(singleobj.get(4))
print(singleobj.get(0))
print(singleobj.get(2))
print("============= set ==============")
print(singleobj.set(15,1))
print(singleobj.set(100,0))
singleobj.print()
print("============ insert ===============")
#singleobj.insert(55,0)
print("lenght of the list: ", singleobj.length)
singleobj.insert(89, 5)
singleobj.insert(98, 5)
singleobj.print()
print("lenght of the list: ", singleobj.length)
print("============ remove ===============")
singleobj.remove(4)
singleobj.print()
print("lenght of the list: ", singleobj.length)
