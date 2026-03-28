#to sort a list using python, in ascending order
import random
list = []
for i in range(10):
    temp = random.randint(1,100)
    list.append(temp)
print("The list is: ", list)
def sort(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list
print("The sorted list is: ", sort(list))
