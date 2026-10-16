from collections import deque
class CustomerServiceQueue:
    def __init__(self):
        self.queue = deque()

    def add_customer(self, customer_name):
        self.queue.append(customer_name)
        print(f"Customer {customer_name} has been added to the queue.")

    def serve_customer(self):
        if self.queue:
            served = self.queue.popleft()
            print(f"{served} has been served.")
        else:
            print("No customers in the queue.")

    def next_customer(self):
        if self.queue:
            print(f"The next customer to be served is {self.queue[0]}.")
        else:
            print("No customers in the queue.")

    def display_queue(self):
        if self.queue:
            print("Current queue:", list(self.queue))
        else:
            print("The queue is empty.")


queue = CustomerServiceQueue()
queue.add_customer("Alice")
queue.add_customer("Bob")
queue.add_customer("Charlie")

queue.display_queue()
queue.next_customer()
queue.serve_customer()
queue.display_queue()   

