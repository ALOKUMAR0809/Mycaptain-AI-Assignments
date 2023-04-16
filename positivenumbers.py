# Taking input from the user
input_list = input("Enter a list of numbers: ")
list_strings = input_list.split(",")
# Convert each string in the list to an integer
list1 = [int(num) for num in list_strings]
# Initialize an empty list to store the positive numbers
positive_numbers = []
# Iterate over each number in the list
for num in list1:
    # Check if the number is positive
    if num > 0
        positive_numbers.append(num)
# Print the positive numbers
print(positive_numbers)
