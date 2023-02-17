list_of_times = [12, 53, 32, "text"]

for counter in range(0, 20, 2):
    print(counter)

for index_in_list, item in enumerate(list_of_times):
    print(f"index: {index_in_list}\tValue: {item}")
    if index_in_list < len(list_of_times) -1:
        list_of_times[index_in_list+1]

for num in range(2, 10):
    if num % 2 == 0:
        