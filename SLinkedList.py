from Node import Node


class SLinkedList:

    def __int__(self):
        self.headVal = None

    def listPrint(self):
        printVal = self.headVal
        while printVal is not None:
            print(printVal.dataVal)
            printVal = printVal.nextVal

    def atBegining(self, newData):
        NewNode = Node(newData)
        NewNode.nextVal = self.headVal
        self.headVal = NewNode

    def atEnd(self, newData):
        NewNode = Node(newData)
        if self.headVal is None:
            self.headVal = NewNode
            return
        laste = self.headVal
        while laste.nextVal:
            laste = laste.nextVal
        laste.nextVal = NewNode

    def RemoveNode(self, RemoveKey):
        HeadVal = self.headVal
        if HeadVal is not None:
            if HeadVal.dataVal == RemoveKey:
                self.headVal = HeadVal.next
                HeadVal = None
                return
        while HeadVal is not None:
            if HeadVal.dataVal == RemoveKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextVal
        if HeadVal is None:
            return
        prev.nextVal = HeadVal.nextVal
        HeadVal = None
