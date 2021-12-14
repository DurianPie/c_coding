class CQueue(object):

    def __init__(self):
        self.append = []
        self.delete = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """



    def deleteHead(self):
        """
        :rtype: int
        """

cmds = eval(input())
val = eval(input())

for cmd in val:
    print(cmd)

result = []
for i, cmd in enumerate(cmds):
    if cmd == 'CQueue':
        result.append([])
    elif cmd == 'appendTail':
        CQueue.appendTail(value = val[i][0])
        result.append([])
    elif cmd == 'deleteHead':
        result.append(CQueue.deleteHead())

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()