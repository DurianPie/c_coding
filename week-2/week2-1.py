class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.pre = None

class LinkList(object):
    def __init__(self, node = None) -> None:
        self.head = node
        self.end = node
    def add(self, item):
        node = Node(item)
        if self.head == None:
            self.head = self.end = node
        else:
            node.pre = self.end
            self.end.next = node
            self.end = node
    def printLinkList(self):
        node = self.head
        while(node != None):
            print(node.elem, end = ' ')
            node = node.next
        print('')
    def spin(self):
        self.end.next = self.head
        self.head.pre = self.end
        self.head = self.end
        self.end = self.end.pre
        self.end.next = None

n, t = map(eval,input().split(' '))
data = map(eval,input().split(' '))
l = LinkList()
for item in data:
    l.add(item)
for _ in range(t):
    l.spin()
l.printLinkList()
