import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable :
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

print(heapsort([1,2,3]))
# heapsort([1,2,3])