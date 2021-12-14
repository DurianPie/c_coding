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

# n, t = map(eval,input().split(' '))
# data = map(eval,input().split(' '))
# l = LinkList()
# for item in data:
#     l.add(item)
# for _ in range(t):
#     l.spin()
# l.printLinkList()

rtk = '/home/robin.wang/git.nevint.com/tensorpiloit/new2/datafilter/data/rtk_files_06/20210601T015553_8N3824_rtk.txt'
rtk_out = 'out.csv'
tag_out = 'tag.json'
gen_path = '/home/robin.wang/git.nevint.com/tensorpiloit/new2/datafilter/datafilter/src/gen_clip_tag.py'
cmd = 'python3 {} {} {} {}'.format(gen_path, rtk, rtk_out, tag_out)
print(cmd)