# Implement your function below.
def most_frequent(given_list):
    max_item = None
    given_list_len = len(given_list)
    if(given_list_len == 0):
        max_item = None
    elif(given_list_len == 1):
        max_item = given_list[0]
    else:
        d = {}
        key = given_list[0]
        for num in given_list:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

            if(d[key] < d[num]):
                key = num
        max_item = key
    return max_item

# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1
list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3
list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list3) should return None
list3 = []
# most_frequent(list4) should return 0
list4 = [0]
# most_frequent(list5) should return -1
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]

print(most_frequent(list1))
print(most_frequent(list2))
print(most_frequent(list3))
print(most_frequent(list4))
print(most_frequent(list5))