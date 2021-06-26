class Node:
    def __init__(self, value, nextn=None, prevn=None):
        self.value = value
        self.next = nextn
        self.prev = prevn

class Linked_list:

    def __init__(self):
        self.head = None #Голова
        self.tail = None #Хвост
        self.length = 0 #Длина 2-х списка
    
    def add(self, value): #add elements in list
        if self.head is None:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            node_1 = Node(value, prevn=self.head)
            self.head.next = node_1
            self.head = node_1
        self.length += 1

    def delele(self, index):
        if self.head is None:
            print('List is empty')
            return 

        if index == 0: # Если индекс равно 0, Удаляем Хвост
            self.tail = self.tail.next # новый хвост равен следующему хвосту старого хвоста
            if self.tail is not None: #Если в списка больше 1 элемента
                self.tail.prev = None  # тогда мы у нового хвоста удаляем ссылку на старый хвост
            self.tail.prev = None # удаляем ссылку
        elif index == self.length - 1:
            self.head = self.head.prev
            if self.head is not None: # если в списке 1 элем, он и голова, и хвост, и prev, и head none. Проверка на то,что в списке больше 1 элемента 
                self.head.next = None
        else: # Если удален из середины
            i = 0 # счетчик
            temp = self.tail # cчетчик запускаем из хвоста # счетчик пускаем из хвоста # temp - текущий узел
            while i <= index -1: #пока
                temp = temp.next
                i += 1
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
        self.length -= 1 #уменьшили длину списка после удаления

    def insert(self, index, value):
        if self.head is None or index >= self.length:
            self.add(value)
            return

        if index <= 0:
            node_1 = Node(value, nextn=self.tail)
            self.tail.prev = node_1
            self.tail = node_1
        else:
            i = 0 # счетчик
            temp = self.tail 
            while i < index: 
                temp = temp.next
                i += 1
            node = Node(value, nextn=temp, prevn=temp.prev) # создали новый узел
            temp.prev = node #написали ссылки
            temp.prev.next = node
        self.length = 1 

    def check(self, value):
        i = 0
        temp = self.tail
        while i <= self.length:
            if temp.value == value:
                return True
            temp = temp.next
            i += 1
        return False    