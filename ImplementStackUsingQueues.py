'''
Implement a last-in-first-out (LIFO) stack using only two queues. 
The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, 
size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or 
deque (double-ended queue) as long as you use only a queue's standard operations.
'''

class MyStack:

    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        return self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def empty(self) -> bool:
        return len(self.stack) == 0

#or

from queue import Queue

class MyStack:

    def __init__(self):
        self.queue = Queue()
    def push(self, x: int) -> None:
        self.queue.put(x)
        for _ in range(self.queue.qsize() - 1):
            self.queue.put(self.queue.get())
    def pop(self) -> int:
        return self.queue.get()
    def top(self) -> int:
        return self.queue.queue[0]
    def empty(self) -> bool:
        return self.queue.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

'''
Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
'''