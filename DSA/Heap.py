import heapq

# Create empty heap
my_heap = []

# Insert elements
heapq.heappush(my_heap, 9)
heapq.heappush(my_heap, 3)
heapq.heappush(my_heap, 5)
print(my_heap) # [3, 9, 5]

# Remove smallest element
print(heapq.heappop(my_heap))  # 3
print(my_heap) # [5, 9]

# Push + Pop in one step
print(heapq.heappushpop(my_heap, 7)) # 5
print(my_heap) # [7, 9]

# Transform list into heap
nums = [5, 7, 3, 1]
heapq.heapify(nums)

my_heap = []
heapq.heappush(my_heap, (3, "A"))
heapq.heappush(my_heap, (2, "B"))
heapq.heappush(my_heap, (1, "C"))

# Removes lowest number = highest priority
print(heapq.heappop(my_heap))  # (1, "C")