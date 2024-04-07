from tkinter import *

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        #self.current = None
    def empty(self):
        return self.head is None
    
    def append(self, data):# at the end
        new_node = Node(data)
        if self.empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):# at the start
        new_node = Node(data)
        if self.empty():
            self.head= self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def print_list(self):
        current = self.head
        text = ""
        while current:
            text += str(current.data) + " "
            current = current.next
        return text

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return False

    def remove(self, data):
        current = self.search(data)
        if current == False:
            print ("no such element")
        else:
            if current.prev:
                current.prev.next = current.next
            else:
                self.head = current.next
            if current.next:
                current.next.prev = current.prev
            return



llist = DoublyLinkedList()
#llist.append("1")
#llist.append("2")
#llist.append("3")

wind = Tk()
wind.title("lab3")
wind.geometry('350x200')

def app():
    llist.append(enter2.get())

def prep():
    llist.prepend(enter2.get())

def rm():
    llist.remove(enter2.get())

def show():
    lbl3.configure(text = "your list: " + llist.print_list())

#lbl = Label(wind, text = "enter text"); lbl.grid()

#entry = Entry(wind, width=57); entry.grid(column = 0, row = 1)

lbl2 = Label(wind, text="enter key", width=30)
lbl2.grid()

enter2 = Entry(wind, width=20)
enter2.grid(column=0, row=1)

btn = Button(wind, text = "remove", fg = "red", command=rm)
btn.grid(column=1, row=0)

btn2 = Button(wind, text = "append", fg = "red", command=app)
btn2.grid(column=1, row=1)

btn3 = Button(wind, text = "prepend", fg = "red", command=prep)
btn3.grid(column=1, row=2)

btn3 = Button(wind, text = "show", fg = "red", command=show)
btn3.grid(column=0, row=7)

lbl3 = Label(wind, text = "your list: " + llist.print_list())
lbl3.grid(column=0, row=8)


wind.mainloop()