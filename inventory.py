
class Stack:
    def __init__(self):
        self.items = []
	
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def display(self):
        for i in range(len(self.items)-1, -1, -1):
            print(self.items[i])
		
stack=Stack()
n=int(input("\nEnter the number of items purchased : "))
for i in range(n):
    a=input("Enter the items : ")
    stack.push(a)
while(1):
    m=int(input("Enter the number of items needed for production : "))
    if(n>=m):
        break
for i in range(m):
    a=input("Enter the items for production : ")
    l=[]
    for j in range(n,0,-1):
        if stack.peek()==a:
            b=stack.pop()
            print(b," is available in position ",j)
            break
        else:
          
            b=stack.pop()
            l.append(b)
                    
    if l!='':
        while len(l)>0:
            stack.push(l.pop())
print("items for which production is not required are:")

stack.display()








