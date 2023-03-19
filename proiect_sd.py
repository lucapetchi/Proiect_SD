import random
import time


def radix_sort(arr, base):

    max_val = max(arr)

    num_digits = 0
    while max_val > 0:
        num_digits += 1
        max_val //= base

    for i in range(num_digits):
        buckets = [[] for _ in range(base)]
        for j in range(len(arr)):
            digit_val = (arr[j] // (base ** i)) % base
            buckets[digit_val].append(arr[j])
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
    return arr

def shellSort(arr, n):

    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval

            arr[j] = temp
        interval //= 2

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def InsertionSort(arr):

    for i in range(1, len(arr)):
        temp = arr[i]

        j = i-1
        while j >=0 and temp < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = temp


def counting_sort(alist, largest):
    c = [0] * (largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1


    c[0] = c[0] - 1
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(alist)


    for x in reversed(alist):
        result[c[x]] = x
        c[x] = c[x] - 1

    return result


def algoritmi(arr):
    #pentru testul alg/counting_Sort
    copie=arr

    start = time.time()
    merge_sort(arr)
    end = time.time()
    print("Timp merge-sort",end - start)
    print(test_sort(arr))
    arr=copie

    start = time.time()
    radix_sort(arr,16)
    end = time.time()
    print("Timp radix-sort", end - start)
    print(test_sort(arr))
    arr = copie

    start = time.time()
    InsertionSort(arr)
    end = time.time()
    print("Timp insertion sort", end - start)
    print(test_sort(arr))
    arr = copie

    start = time.time()
    shellSort(arr,len(arr))
    end = time.time()
    print("Timp shell_sort", end - start)
    print(test_sort(arr))
    arr = copie

    start = time.time()
    counting_sort(arr,max(arr))
    end = time.time()
    print("Timp counting_sort", end - start)
    print(test_sort(arr))
    arr = copie

    start = time.time()
    arr.sort()
    end = time.time()
    print("Timp sort nativ", end - start)
    print(test_sort(arr))


def test_sort(arr):
    k=True
    for i in range(0,len(arr)-1):
       if (arr[i]>arr[i+1]):
           k=False
    return k

T=int(input("Introduceti numarul de teste: "))

def teste(T):
    K=0
    while(K<T):
        print("Testul nr:",K)
        min=int(input("min: "))
        max=int(input("max: "))
        n=int(input("Nr numere:"))
        arr_random = []
        arr_sorted = []
        arr_reverse = []
        for i in range(0, n):
            c = n - i
            arr_random.append(random.randint(min, max))
            #arr_sorted.append(i)
            #arr_reverse.append(c)

        algoritmi(arr_random)
        K=K+1



print(teste(T))
#p=[1,2,4,6,2,3,6,4,1,2,3,5,6,32,423,431,42,1191,92]
#quickSort(p,0,len(p)-1)
#print(p)
