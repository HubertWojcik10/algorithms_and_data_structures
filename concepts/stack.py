class Stack:
    '''My own implementation of the stack data structure)'''
    def __init__(self):
        self._stack = [None]
        self._n = 0

    def push(self, value):
        if len(self._stack) == self._n:
            self._resize(2 * self._n)
        
        self._stack[self._n] = value
        self._n += 1
    
    def pop(self):
        if len(self._stack) == 0:
            raise IndexError('Stack is empty')

        popped = self._stack[self._n-1]
        self._stack[self._n-1] = None
        self._n -= 1

        if self._n > 0 and len(self._stack) > self._n//4:
            self._resize(len(self._stack)//2)
        
        return popped

    def peek(self):
        return self._stack[self._n-1]

    def _resize(self, new_size):
        tmp = [None] * new_size
        for i in range(self._n):
            tmp[i] = self._stack[i]
        
        self._stack = tmp


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2) 
    stack.push(3)
    stack.pop()
    print(stack.peek())