class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i - 1) // 2
        
    def left_child(self, i):
        return 2 * i + 1
        
    def right_child(self, i):
        return 2 * i + 2
        
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def insert(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
        
    def _sift_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)
            
    def display(self):
        print(self.heap)
    
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if len(self.heap) > 0:
            self._sift_down(0)
        
        return max_val

    def _sift_down(self, i):
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right
            
        if i != max_index:
            self.swap(i, max_index)
            self._sift_down(max_index)

# Reuse the heap from exercise 1
heap = MaxHeap()
values = [5, 3, 8, 1, 2, 7, 6, 4]
for value in values:
    heap.insert(value)

print("Initial Max Heap:", end=" ")
heap.display()

print("\nExtracting max values:")
for _ in range(3):
    max_value = heap.extract_max()
    print(f"Extracted: {max_value}, Current Heap:", end=" ")
    heap.display()
