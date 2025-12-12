

def linear(array, target):
    for i in range(len(array)):
        if array[i]== target:
            return i
number = [1,2,3,4,5,6,7,8,9]
search_for = 5


result_index = linear(number, search_for)

if result_index != -1:
    print(f"Target **{search_for}** found at index: **{result_index}**")
    print(f"To verify: number[{result_index}] is {number[result_index]}")
else:
    print(f"Target **{search_for}** was not found in the list.")


