# a=["a","i",'e',"o","u"]
# a_=["a",7,"b","w",9]
# removed_list=[]
# for i in a_:
#     if i in a:
#         removed_list.append(i)

#     elif type(i) == int:
#         removed_list.append(i)
# print(removed_list)


a=["a","i",'e',"o","u"]
a_=["a",7,"b","w",9]
removed_list=[]
for i  in a_:
    if i not in a:
        removed_list.append(i)

    elif type(i) != int:
        removed_list.append(i)
print(removed_list)
