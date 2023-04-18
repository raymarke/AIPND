# # # my_dict = {'apple': 1, 'banana': 2, 'orange': 3}

# # # for key in my_dict:
# # #     print(key, my_dict[key])

# my_str = 'dalmatian, dalmatian, coach dog, carriage dog'
# my_list = my_str.split(', ')

# # print(for name in names my_str.split(', ')[name])
# matches = [match for match in my_list if "dalmatian" in match]
 
# print(matches)

# # d = {}
# # with open("dognames.txt") as f:
# #     for line in f:
# #         key = line.strip('\n')
# #         d[key] = 1
# #         # (key, val) = line.split()
# #         # d[int(key)] = val

# # print (d)

# import pandas as pd
# table = [[1, 2222, 30, 500], [4, 55, 6777, 1]]
# df = pd.DataFrame(table, columns = ['a', 'b', 'c', 'd'], index=['row_1', 'row_2'])
# print(df)

from tabulate import tabulate
# table = [['col 1', 'col 2', 'col 3', 'col 4'], [1, 2222, 30, 500], [4, 55, 6777, 1]]
# print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

table = [[1, 2222, 30, 500], [4, 55, 6777, 1]]
print(tabulate(table, tablefmt='fancy_grid'))