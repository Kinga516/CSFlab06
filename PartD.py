"""Part D: Integration with Data Structures."""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def to_list(self):
        return self.items.copy()


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def to_list(self):
        return self.items.copy()


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def linear_search(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1


def main():
    print("Task 7: Stack + Sorting")
    stack = Stack()
    elements = [64, 25, 12, 22, 11]
    for elem in elements:
        stack.push(elem)
    print("Stack elements pushed:", elements)
    stack_list = stack.to_list()
    print("Stack as list:", stack_list)
    sorted_list = selection_sort(stack_list.copy())
    print("Sorted list:", sorted_list)
    print()

    print("Task 8: Queue + Searching")
    queue = Queue()
    queue_elements = [10, 20, 30, 40, 50]
    for elem in queue_elements:
        queue.enqueue(elem)
    print("Queue elements enqueued:", queue_elements)
    queue_list = queue.to_list()
    print("Queue as list:", queue_list)
    search_element = 30
    position = linear_search(queue_list, search_element)
    if position != -1:
        print(f"Element {search_element} found at position {position}")
    else:
        print(f"Element {search_element} not found")


if __name__ == "__main__":
    main()