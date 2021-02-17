# # LIST SLICING

# my_list = list(range(21))
# print(my_list)
# print(my_list[2])

# # slice from 0-4

# my_slice = my_list[0:5]
# print(my_slice)

# # slice from 5 - 15

# my_slice= my_list[5:16]
# print(my_slice)
# # slice with interval
# # slice takes [start:stop:step]

# my_slice = my_list[1:19:2]
# print(my_slice)

# [ade, jonah, seun] = [23, 45, 66]
# print(ade)
# print(jonah)

# len min and max builtin functions
# my_list = ["ade", "kunle", "salami", "sobayo", "richard"]
# x = len(my_list)
# print(x)
# x = min(my_list)
# print(x)
# x = max(my_list)
# print(x)

# print(['foo', 'bar', 'baz', 'qux', 'quux', 'corge'][2])
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
# print(len(x))
# for i in x:
#     print(i)

# print(x[1][1][0]) # deep indexing for a nested list 