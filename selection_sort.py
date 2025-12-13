def selection_sort(input_arr):
    n = len(input_arr)
    for i in range (n):
        mini = i
        for j in range(i+1,n):
            if input_arr[j] < input_arr[mini]:
                mini=j
            input_arr[i], input_arr[mini]=input_arr[mini], input_arr[i]

input_arr = [64,25,12,22,11]

selection_sort(input_arr)

print("original array is:", [64,25,12,22,11])
print("sorted list is here:", input_arr)