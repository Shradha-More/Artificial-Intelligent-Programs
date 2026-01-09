# Selection Sort using Greedy Algorithm
def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]

# Driver Code
alist = list(map(int, input("Enter the list of numbers separated by space: ").split()))
selection_sort(alist)
print("Sorted list:", alist)
