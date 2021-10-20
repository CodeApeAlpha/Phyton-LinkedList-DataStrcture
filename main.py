from SLinkedList import SLinkedList

from Node import Node

list = SLinkedList()

list.headVal = Node('Mon')

Node2 = Node("Tue")
Node3 = Node("Web")

# Link first Node to second
list.headVal.nextVal = Node2

# Link second Node to third node
Node2.nextVal = Node3

list.atBegining("Sun")
list.atEnd("Thu")

list.RemoveNode("Tue")
list.listPrint()
