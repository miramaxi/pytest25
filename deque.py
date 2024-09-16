from collections import deque
from queue import LifoQueue

stack = deque([1, 2, 3])
stack.append(4)
stack.appendleft(0)
value = stack.pop()
value2 = stack.popleft()
print(stack)
print(value)
print(value2)
# Для добавления элементов 
# списка в другой список используй метод extend().