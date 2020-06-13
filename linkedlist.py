class Node:
    def __init__(self, data=None):
        self.data = data 
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printing(self):
        printvalue = self.head
        while printvalue is not None:
            print(printvalue.data)
            printvalue = printvalue.next

    def beg(self, data3):
        new = Node(data3)
        new.next = self.head
        self.head = new

    def end(self, data4):
        new = Node(data4)
        if self.head is None:
            self.head = new
            return
        lastNode = self.head
        while(lastNode.next):
            lastNode = lastNode.next
        lastNode.next = new

    def between(self, node, datapart):
        new = Node(datapart)
        new.next = node.next
        node.next = new

    def delNode(self,deldata):
        new = self.head
        if new is not None:
            if new.data == deldata:
                self.head = new.next
                new = None 
                return
        while new is not None:
            if new.data == deldata:
                break
            prev = new
            new = new.next
        if (new == None):
            return
        prev.next = new.next
        new = None

x = LinkedList()
x.head = Node("mohmmad")
data1 = Node("mohammadi")
data2 = Node("iran")

x.head.next = data1
data1.next = data2
x.beg("sara")
x.end("jafar")
x.between(x.head,"between")

x.delNode("mohammadi")

x.printing()
