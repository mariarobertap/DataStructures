class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        node = self.head
        mylinkedlist = ''
        while node != None:
            mylinkedlist += str(node.data)+'  -->  ' if node.next else str(node.data)
            node = node.next

        print(mylinkedlist)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

       
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        node  = self.head
        while node != None:

            if count == index - 1:
                node = Node(data, node.next)
                node.next = node
                break

            node = node.next
            count += 1


    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        node = self.head
        while node != None:

            if count == index - 1:
                
                deletedNode = node.next
                node.next = deletedNode.next

                del deletedNode

                break

            node = node.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    myLinkedList = LinkedList()
    myLinkedList.insert_values(["banana","mango","grapes","orange", "abacate"])
    myLinkedList.print()
    myLinkedList.remove_at(2)
    myLinkedList.print()


   # myLinkedList.insert_at(1,"blueberry")
   # myLinkedList.print()
    #myLinkedList.remove_at(2)
    #myLinkedList.print()

    #myLinkedList.insert_values([45,7,12,567,99])
    #myLinkedList.insert_at_end(67)
    #myLinkedList.print()