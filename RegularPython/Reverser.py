user_input = input("Enter a string to reverse: ")
list_user_input = user_input.split()
j = len(list_user_input)
print("Reversed string: ", end='')
while j > 0:
    print(list_user_input[j-1], end=" ")
    j -= 1