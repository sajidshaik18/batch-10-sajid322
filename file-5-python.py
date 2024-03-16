# ! ------> common functions for list

#l1 = [6, 7, 8, 9, 0]
#print(len(l1))

#print(max(l1))
#print(min(l1))

#l1 = [6, 8, 9, "P", "u"]
#print(max(l1)) # --> error coz its a combination of list and string
#print(min(l1)) # --> error coz its a combination of list and string

#l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# index() --> to get index value of specific element
#print(l1.index(9))

#l1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
# count()--->how many num of times an element is repeated
# print(11.count(6))

# ! some functions which is specifically used for list

# to add element inside list
# ? insert(index_value, element) --> to add element at specific index position
# l1 = [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]
# l1.insert(2, "cars")

# ? to delete element from list
l1 = [6,6,6, 7, 8, 9, 0, 8.89, 5, 0.78]
# pop() ---> last element will be deleted
# l1.pop()
# print(l1)

# *pop(index_value) --> used to delete element at specific index
# l1.pop (4) # 4 is index value
# print(l1)


# *remove(element) --> used to delete element directly
# l1.remove(8.89)
# print (l1)

#* clear() --> to complete delete all element in list
# l1.clear()
# print(l1)

# del -> to delete the list
# del l1 #or del(l1)
# print(l1)

# ? ----> join to lists

l1 = [9, 0, 8]
l2 = ["p","o","t",34]
# * print(l1+l2)

# ! or

# * extend() --> to combine 2 lists
# l1.extend(l2)
# print(l1)

# ? ------> copy()
# l1 = [6, 7, 8, 9, 3]
# l2 = l1.copy()
# print(l2)
# print(l1)

# print(id(l1))
# print(id(l2))

# ! diff between shallow copy and deep copy
# * shallow copy
# import copy
# l1 = [8, 9, 0,[5, 6], [3, 2, 1]]
# l2 = copy.copy(l1)
# l1.append(890)
# print(l1)
# print(l2)


# * deep copy --> used to copt the list with nested list
# import copy
# l1 = [8, 9, 0,[5, 6], [3, 2, 1]]
# print(l1[-1][1]) --> to index nested list

# l2 = copy.copy(l1)
# l1[-1].append('cars')
# print(l1)
# print(l2)

# ? sort --> arrange elements in list in ascending or descending order
l1 = [9, 7, 45,0,-6, 5, 12]
# l1.sort() # to arrange in ascending in descending order
# print(l1)

# l1.sort(reverse=true) # to sort in descending order
# print(l1)

# l1 = ['z', 'i', 'o', 'p', 9]
# l1.sort()
# print(l1) # --> error

# ? list constructor
# * list() --> to convert other collection datatype to list
# l3 = ((8,9,0))
# print(list(13))

# l4 = 8
# print(list(14))

# ! ---> nested list

l1 = [8, 9, [0,8,7], ["p", "o", "y"], [8, 't']]
# print(l1[-2][1]) # --> o

# print(l1[1:4])
# print(l1[1:-1])

# ? to delete "t" from l1
# l1[-1].remove('t')
# print(l1)

# ? combine these ["p", "o", 'y'], [8, 't'] list in l1 to ["p", "o", "y", 8, 't']
# l1[-2].extend(l1[-1})
# l1.pop(-1)
# print(11)

# ! ------> tuple
# *char of tuple

# 1.) tuple have to be surrended by()
# 2.) the elements inside tuple are not changable
# 3.) the elements inside tuple are indexed
# 4.) the element will execute in order
# 5.) it is heterogenous
# 6.) it allow duplicate element

# eg:
t1 = (8,8,9,6,5.78, [9,0], (6, 8), "hey", 9+6j)
# print(t1)
# print(type(t1))

# ? indexing, slicing are all same as list

# ? ways to create tuple
# l1 = (8)
# print(type(l1)) # int

# l1 = (8)
# print(type(l1)) # tuple

# t1 = 8,9
# print(type(t1)) # tuple

# t2 = 8,
# print(type(t2)) # tuple

# len(), min(), max(), index(), count(), ---> all same as list

# to add element inside tuple  ---> cannot add
# cannot delete any element from tuple

# * join 2 tuples
# t1 = (8,9,0)
# t2 = (6,7,8)
# print(t1+t2)

# * to add all element inside list
# sum()
l1 = [8, 9, 7, 6]
# print (sum(t1))

# * sort tuple
# t1 = (8, 9, 7, 89, 12)
# print(tuple(sorted(t1)))
# print(tuple(sorted(t1,reverse=true)))

# ? iterate list and tuple

# * iterate based on elements
# l1 = [9, 8, 0, 6, 5]
# for i in l1:
#    print(i)

# * iterate based on index value
# l1 = [9, 8, 0, 6, 5, 8, 56]
# for i in range(0,len(l1)):
#   print(l1[i])

# print (l1[2])


