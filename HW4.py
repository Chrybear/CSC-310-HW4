#   Author: Charles Ryan Barrett
#   CSC 310 HW4
#   Date: 2/23/2019
#   Sources:
#   The class "LL" is mostly taken from the example Queue linked list python file in class documents, "linked_queue.py"
## Problem 1 work area
class Deque:  # Creating the que class
    def __init__(self,x): #constructor
        self.max_size = x
        self.Q = [None]*self.max_size #making a blank list x long
        self.size = 0
        self.front = -1
        self.rear = -1

    def lenn(self): #returns the number of elements in the list
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def getFront(self): #return the element in the front
        #print("front = ", self.front)
        if self.is_empty():
            return -1
        else:
            print(self.Q[self.front])


    def getRear(self):
        #print("rear = ",self.rear)
        if self.is_empty():
            return -1
        else:
            print(self.Q[self.rear])



    def insertLast(self,x): #adds an element to the rear
        if self.is_full():
            return False
        else:
            if self.front == -1: # for when one of the front is -1 and rear >=0
                self.front+=1

            self.size+=1

            if self.rear != self.max_size - 1:
                self.rear += 1
                self.Q[self.rear] = x

            else:       # Wrap around to the beginning
                self.rear = 0
                self.Q[self.rear] = x
        #print("rear = ",self.rear)
        return True     #operation was succesful


    def insertFront(self,x):
        if self.is_full():
            return False
        else:
            if self.front == -1: # in case it is the first addition of an element
                self.front+=1

            # front will stay the same, but rear changes so needs to be updated
            if self.rear != self.max_size - 1:
                self.rear += 1
            else:  # Wrap around to the beginning
                self.rear = 0

            i = 0           # I want to loop max_size times
            k = self.front
            tmp = x
            #print("before loop front = ",self.Q[self.front])
            self.size+=1
            while i < self.max_size:
                if k != self.max_size:
                    tmp2 = self.Q[k]
                    self.Q[k] = tmp
                    #print("Inside loop",self.Q[k],"self front = ",self.Q[self.front])
                    tmp = tmp2
                    k+=1    # incrementing k
                else:   #k circled back to start
                    k = 0 #resetting to beginning
                    tmp2 = self.Q[k]
                    self.Q[k] = tmp
                    #print("Inside loop, else ", self.Q[k])
                    tmp = tmp2

                    k+=1    # incrementing k
                #print("After loop front ", self.Q[self.front])

                i+=1 # incrementing i
            #print("Que = ",self.Q)
            #print("front = ",self.front)
            return True

    def deleteFront(self):
        if self.is_empty():
            return False
        else:
            self.Q[self.front] = None
            if self.front != self.max_size-1:
                self.front+=1
            else:
                self.front = 0
            self.size-=1
            return True

    def deleteLast(self):
        if self.is_empty():
            return False
        else:
            self.Q[self.rear] = None
            if (self.rear-1) < 0:
                self.rear = self.max_size-1
            else:
                self.rear -= 1
            self.size -= 1
            return True

##   Problems 2 and 3 work area

#setting up class to create a linked list

class LL: # Linked list class
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    class _node:  # node class
        def __init__(self, x, nxt):
            self.data = x
            self.next = nxt


    def lenn(self):
        return self.size

    def is_empty(self):
        return self.size == 0


    def first(self):
        if self.is_empty():
            print("The Linked List is empty!")
        else:
            return self.head.data

    def enque(self,x): # adding values to the LL
        new_node = self._node(x,None)
        # Need to check if list is empty
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size +=1

    def deque(self):
        if self.is_empty():
            print("The Linked List is empty!")
        else:
            value = self.head.data
            self.head = self.head.next
            self.size -=1

            if self.is_empty():
                self.tail = None
            return value

    def search(self,x):
        # print("x = ",x)
        index = self.head
        # print("index = ", index)
        while index != None:
            if index.data == x:
                return True
            index = index.next
        return False # linked list was searched, but specific value not found


    def printLL(self): # this method will print a LL
        i = self.head
        output = ""
        while i != None:
           output += (str(i.data) + " -> ")
           i = i.next
        print(output[:-3]) # gets rid of the last arrow
        print()


### Input area

## problem 1 inputs
go = True
size_of_queue = int(input("Enter the size of the Circular Queue: "))
DQ = Deque(size_of_queue)



while go:
    print()
    print("Circular Queue menu")
    print()
    print("1: Test if Full")
    print("2: Test if Empty")
    print("3: Get front value")
    print("4: Get rear value")
    print("5: Insert a value into the front of the queue")
    print("6: Insert a value into the rear of the queue")
    print("7: Delete the first value in the queue")
    print("8: Delete the last value in the queue")
    print("9: Print the Queue")
    print("0: Exit")
    inny = int(input("Select: "))

    if inny == 1:
        print(DQ.is_full())
    if inny == 2:
        print(DQ.is_empty())
    if inny == 3:
        DQ.getFront()
    if inny == 4:
        DQ.getRear()
    if inny == 5:
        val = input("Enter value to insert at the front: ")
        print(DQ.insertFront(val))
    if inny == 6:
        val = input("Enter value to insert at the rear: ")
        print(DQ.insertLast(val))
    if inny == 7:
        print(DQ.deleteFront())
    if inny == 8:
        print(DQ.deleteLast())
    if inny == 9:
        print(DQ.Q)
    if inny == 0:
        print("So long!")
        go = False


## input for problems 2 & 3
L1 = LL()
L2 = LL()
print()
#L1.enque(1)
#L1.enque(2)
#L1.enque(4)

#L2.enque(1)
#L2.enque(3)
#L2.enque(4)

go = True

while go:
    print()
    print("Linked List menu")
    print()
    print("1: Enqueue Linked List 1")
    print("2: Enqueue Linked List 2")
    print("3: Length of the lists")
    print("4: Are the lists empty?")
    print("5: Dequeue Linked List 1")
    print("6: Dequeue Linked List 2")
    print("7: First item in both lists")
    print("8: Search both lists for a number")
    print("9: Print both Linked Lists")
    print("10: Merge the two lists")
    print("0: Exit")
    inny = int(input("Selection: "))

    if inny == 0:
        print("Goodbye!")
        go = False
    if inny == 1:
        num = int(input("Enter the number to add to Linked List 1: "))
        L1.enque(num)
    if inny == 2:
        num = int(input("Enter the number to add to Linked List 2: "))
        L2.enque(num)
    if inny == 3:
        print("L1 = ",L1.size)
        print("L2 = ",L2.size)
    if inny == 4:
        print("Is L1 empty? ",L1.is_empty())
        print("Is L2 empty? ",L2.is_empty())
    if inny == 5:
        L1.deque()
    if inny == 6:
        L2.deque()
    if inny == 7:
        print("First in L1 = ",L1.first())
        print("First in L2 = ",L2.first())
    if inny == 8:
        num = int(input("Enter the number to be searched: "))
        print("Is ",num," in L1? ", L1.search(num))
        print("Is ",num," in L2? ", L2.search(num))
    if inny == 9:
        print("L1: ", end='')
        L1.printLL()
        print("L2: ", end='')
        L2.printLL()
        print()
    if inny == 10:
        #I tried to make this a method, but it didn't seem to work
        L3 = LL()  # linked list that will be the merge of L1 and L2
        #i = max(L1.size, L2.size)
        in1 = L1.head
        in2 = L2.head
        if L1.size == L2.size:  # if they are the same size
            while in1 != None:
                L3.enque(in1.data)
                L3.enque(in2.data)
                in1 = in1.next
                in2 = in2.next
        elif L1.size > L2.size:  # L1 is larger
            while in2 != None:
                L3.enque(in1.data)
                L3.enque(in2.data)
                in1 = in1.next
                in2 = in2.next
            while in1 != None:
                L3.enque(in1.data)
                in1 = in1.next
        elif L2.size > L1.size:  # L2 is larger
            while in1 != None:
                L3.enque(in2.data)
                L3.enque(in2.data)
                in1 = in1.next
                in2 = in2.next
            while in2 != None:
                L3.enque(in2.data)
                in2 = in2.next
        print("L1 and L2 merged: ", end='')
        L3.printLL()

