
# List Operations
my_list = [1, 2, 3,4,5]
print("Original List:", my_list)
# Adding elements to the list
my_list.append(4)
print("List after adding 4:", my_list)
# Removing an element from the list
my_list.remove(2)
print("List after removing 2:", my_list)
# Modifying an element in the list
my_list[2] = 10
print('List after modifying index 1:', my_list)
print("\n")
# Dictionary Operations
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", my_dict)
# Adding a new key-value pair
my_dict['d'] = 4
print("Dictionary after adding ('d': 4):", my_dict)
# Removing a key-value pair
my_dict.pop('b')
print("Dictionary after removing 'b':", my_dict)
# Modifying a value in the dictionary
my_dict['a'] = 10
print("Dictionary after modifying 'a':", my_dict)

# Set Operations
my_set = {1, 2, 3}
print("Original Set:", my_set)

# Adding an element to the set
my_set.add(4)
print("Set after adding 4:", my_set)

# Removing an element from the set
my_set.discard(2)
print("Set after removing 2:", my_set)
my_set.discard(3)
my_set.add(10)
print("Set after replacing 3 with 10:", my_set)

