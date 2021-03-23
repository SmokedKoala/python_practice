#        x1
#     /       \
#    x0         x3
#  / |  \     /    \
# 11 x2  x3   x0    x2
#  / | \ / \ / | \ / | \
# 10 9 8 7 6 5 4 3 2 1 0


#        0
#     /       \
#    1          2
#  / |  \     /    \
# *  3   4     5     6
#  / | \ / \ / | \ / | \
# *  * * * * * * * * * *

# словарь с обозначением вершины x[i] в ключ - номер вершины(смотри схему сверху), значениями i и номерами вершин-наследников
convert_to_numbers_dict = {
    '0':[1,['1','2']],
    '1':[0,[11,'3','4']],
    '2':[3,['5','6']],
    '3':[2,[10, 9, 8]],
    '4':[3,[7,6]],
    '5':[0,[5,4,3]],
    '6':[2,[2,1,0]]}
# словарь со связями между вершинами
connection_dir = {0:['grace','gdb','flux'], 1:['nsis','zimpl'], 2:['cool','nit','vala'], 3:[1997,2020]}

def f21 (x):
    root = '0'
    # так как у меня корень дерева - x[1], начну отталкиваться от него
    root_node =convert_to_numbers_dict[root][1][connection_dir[1].index(x[1])]
    return f21_recurcive_part(x,root_node)

def f21_recurcive_part(x,root_node):
    if not root_node in convert_to_numbers_dict.keys():
        return root_node
    else:
        current_index = convert_to_numbers_dict[root_node][0]
        return f21_recurcive_part(x,convert_to_numbers_dict[root_node][1][connection_dir[current_index].index(x[current_index])])


if __name__ == "__main__":
    print(f21(['flux','nsis','cool',1997]))
    print(f21(['gdb','zimpl','nit',2020]))
    print(f21(['grace','nsis']))
    print(f21(['grace','nsis','vala']))