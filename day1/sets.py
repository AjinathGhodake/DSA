# 1.	Create a set from a list and remove duplicates:
# •	Input: [1, 2, 2, 3, 4, 4, 5]
# •	Expected output: {1, 2, 3, 4, 5}

unique_elements = set([1, 2, 2, 3, 4, 4, 5])
print("Remove duplicates. Expected output: {1, 2, 3, 4, 5}>>>", unique_elements)


# 2.	Find the union of two sets:
# •	Set 1: {1, 2, 3}
# •	Set 2: {3, 4, 5}
# •	Expected output: {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("union of two sets. Expected output: {1, 2, 3, 4, 5}>>>", set1.union(set2))
print("union of two sets. Expected output: {1, 2, 3, 4, 5}>>>", set1 | set2)

# 3.	Find the intersection of two sets:
# •	Set 1: {10, 20, 30}
# •	Set 2: {20, 30, 40}
# •	Expected output: {20, 30}


set1 = {10, 20, 30}
set2 = {20, 30, 40}
print("intersection of two sets. Expected output: {20, 30}>>>", set1.intersection(set2))
print("intersection of two sets. Expected output: {20, 30}>>>", set1 & set2)

# 4.	Find the difference between two sets:
# •	Set 1: {1, 2, 3, 4}
# •	Set 2: {3, 4, 5, 6}
# •	Expected output: {1, 2}

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("difference between two sets. Expected output: {1, 2}>>>", set1.difference(set2))
print("difference between two sets. Expected output: {1, 2}>>>", set1 - set2)
