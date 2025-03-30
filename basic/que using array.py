"""Implement a Queue using an Array. Queries in the Queue are of the following type:
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop an element from the queue and print the popped element. If the queue is empty then return -1)

We just have to implement the functions push and pop and the driver code will handle the output.

Examples:

Input: Queries = 1 2 1 3 2 1 4 2
Output: 2 3
Explanation: For query 1 2 the queue will be {2} 1 3 the queue will be {2 3} 2   poped element will be 2 the queue will be {3} 1 4 the queue will be {3 4} 2 popped element will be 3 

Input: Queries = 1 3 2 2 1 4   
Output: 3 -1
Explanation: For query 1 3 the queue will be {3} 2 popped element will be 3 the queue will be empty 2 there is no element in the queue and hence -1 1 4 the queue will be {4}. 

Input: Queries = 1 3 2 2 1 3   
Output: 3 -1
Explanation: For query 1 3 the queue will be {3} 2 popped element will be 3 the queue will be empty 2 there is no element in the queue and hence -1 1 3 the queue will be {3} and hence -1 1 3 the queue will be {3}."""



class MyQueue:
    def __init__(self):
        self.arr = []  # Initialize an empty list as queue
    
    # Function to push an element x in the queue.
    def push(self, x):
        self.arr.append(x)  # Add element to the end of the queue
    
    # Function to pop an element from queue and return that element.
    def pop(self): 
        if not self.arr:
            return -1  # Return -1 if queue is empty
        return self.arr.pop(0)  # Remove and return the front element

# Function to process the queries
def processQueries(queries):
    queue = MyQueue()
    result = []
    
    i = 0
    while i < len(queries):
        if queries[i] == 1:  # Push operation
            i += 1
            queue.push(queries[i])
        elif queries[i] == 2:  # Pop operation
            result.append(queue.pop())
        i += 1
    
    print(" ".join(map(str, result)))

# Example Test Cases
processQueries([1, 2, 1, 3, 2, 1, 4, 2])  # Output: 2 3
processQueries([1, 3, 2, 2, 1, 4])  # Output: 3 -1
processQueries([1, 3, 2, 2, 1, 3])  # Output: 3 -1
