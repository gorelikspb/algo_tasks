class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class HashTable:
    def __init__(self, n):
        self.n = n
        self.buckets = [None]*self.n
        
    def hash(self, value):
        return value%self.n

    def insert(self, value):
        index = self.hash(value)
        node = self.buckets[index]
        if not node:
            self.buckets[index] = Node (value) #first element
        else:
            while node:
                prev = node
                node = node.next
            new_node =  Node(value)
            prev.next = new_node


#input example:
# 5
# 5 100 10 24 13

n = int(input())
elements = map(int, input().split())

#input adding
ht = HashTable(n)
for el in elements:
    ht.insert(el)

#output
for i, bucket in enumerate(ht.buckets):
    print (str(i) + ':', end = ' ')
    if bucket:
        node = bucket
        while node:
            print (node.value, end = ' ')
            node = node.next
    print()



# class Node:
#     def __init__(self, value):
#         # self.key = key
#         self.value = value
#         self.next = None


# хеш таблица - массив первых элементов

# 100 на 5, хэш 0

# размер и будет равен хэшу

# my_array = array('i', [])
# if (my_array[0]):
#     print('exist')
