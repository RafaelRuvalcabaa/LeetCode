class Linked: 
    def __init__(self, val=0): 
        self.val = val
        self.next = None

    def __str__(self):
        return f"El valor es: {self.val}"


node1 = Linked(1)
node2 = Linked(2)
node3 = Linked(3)

node1.next = node2
node2.next = node3


val  = node1
while val:
    print(val)
    val = val.next