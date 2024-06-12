# Write a Python program to find the common elements between two lists using a
# for loop.
# List1 = [1,2,3]
# List2 = [4,5,1] # common element is 1

list1 = [1, 2, 3]
list2 = [4, 5, 1]

common_elements = []

for element in  list1:
    if element in list2:
        
        common_elements.append(element)
        
print("Common element: ", common_elements)