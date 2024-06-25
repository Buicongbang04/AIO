from stack import Stack

stack1 = Stack(5)
stack1.push(1)
stack1.push(2)

print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())