def bubblesort(arr):
    k=len(arr)

    for i in range (k-1):
        for j in range (0,k-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr = [76,78,34,21,22,19]

bubblesort(arr)
print("sorted array is")
for i in range (len(arr)):
    print("% d"% arr[i])