class Queue:
    def __init__(self):
        self.queue = []  # Create an empty list
    
    def enqueue(self, item):
        """Adds an item to the end of the queue."""
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Removes an item from the front of the queue."""
        if not self.is_empty():
            removed_item = self.queue.pop(0)
            print(f"Dequeued: {removed_item}")
            return removed_item
        else:
            print("Queue is empty!")

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.queue) == 0

    def front(self):
        """Returns the first element in the queue without removing it."""
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty!")
            return None

    def display(self):
        """Displays the queue."""
        print("Queue:", self.queue)

# Example usage:
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
