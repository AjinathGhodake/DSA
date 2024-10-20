# A tuple of integers
coordinates = (10, 20, 30)

# A tuple of mixed data types
person = ("John", 25, "Programmer")

# A tuple with a single element (needs a trailing comma)
single_element = (5,)


print(coordinates, person, single_element)


# 1.	Create a tuple of your favorite 3 fruits:
# •	Access the second fruit by indexing.
# •	Try to modify one fruit and see what error you get.
fruits = ("Banana", "Apple", "Grapes")
print("Tupples>>>", fruits[1])
# fruits[1] = "Mango"
# print("Tupples>>>", fruits)

# 2.	Use tuple unpacking:
# •	Create a tuple of 3 integers and unpack them into 3 variables.
# •	Print each variable.

integers = 1, 2, 3
print("Integers>>>", integers)
a, b, c = integers
print("a,b,c>>>>", a, b, c)

# 3.	Count method:
# •	Create a tuple with repeated values (e.g., (1, 2, 2, 3, 4, 2)).
# •	Use the count() method to count how many times 2 appears.
repeated_value = (1, 2, 2, 3, 4, 2)
print("Repeated values>>>>>>>", repeated_value)
print("Number of times", repeated_value.count(2))

# 4.	Use a tuple as a dictionary key:
# •	Create a dictionary where the key is a tuple representing coordinates (e.g., (x, y)).

coordinates = {(1, 2): "point1", (2, 3): "point3", (3, 4): "point4"}
print("Coordinate>>>", coordinates[(1, 2)])
