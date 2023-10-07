import sorting
import random

def main():
    n = 100000
    
    # list = [random.randint(1, n) for i in range(n)]
    # print("Bubble Sort")
    # print("Antes: ", list)
    # sorting.bubble_sort(list)
    # print("Depois", list)

    # list = [random.randint(1, n) for i in range(n)]
    # print("Insertion Sort")
    # print("Antes: ", list)
    # sorting.insertion_sort(list)
    # print("Depois", list)    
    
    # list = [random.randint(1, n) for i in range(n)]
    # print("Merge Sort")
    # print("Antes: ", list)
    # sorting.merge_sort(list)
    # print("Depois", list)

    # list = [random.randint(1, n) for i in range(n)]
    # print("Quick Sort")
    # print("Antes: ", list)
    # list = sorting.quick_sort(list)
    # print("Depois", list)

    list = [random.randint(1, 1000) for i in range(n)]
    print("Selection Sort")
    print("Antes: ", list)
    sorting.selection_sort(list)
    print("Depois", list)

    # list = [random.randint(1, n) for i in range(n)]
    # print("Heap Sort")
    # print("Antes: ", list)
    # sorting.heap_sort(list)
    # print("Depois", list)



if __name__ == "__main__":
    main()