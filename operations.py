# Taking input from user
set1 = set(input("Enter the first set (comma-separated values): ").split(','))
set2 = set(input("Enter the second set (comma-separated values): ").split(','))

# Performing set operations
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
diff_set = set1.difference(set2)
symmetric_diff_set = set1.symmetric_difference(set2)

# Printing the result
print("Union of Set1 and Set2: ", union_set)
print("Intersection of Set1 and Set2: ", intersection_set)
print("Difference of Set1 and Set2: ", diff_set)
print("Symmetric Difference of Set1 and Set2: ", symmetric_diff_set)
