# a=["a","i",'e',"o","u"]
# a_=["a",7,"b","w",9]
# removed_list=[]
# for i in a_:
#     if i in a:
#         removed_list.append(i)

#     elif type(i) == int:
#         removed_list.append(i)
# print(removed_list)





student_list=[]
student1={'std1':{"name":"nusu","id":11,"maths":89,"science":78,"english":99},
        'std2':{"name":"nida","id":22,"maths":85,"science":67,"english":34},
          'std3':{"name":"fida","id":33,"maths":34,"science":47,"english":98}}

students=['std1','std2','std3']
for key_ in students:
    student_list.append({"name":key_,"average score":int(sum((student1[key_]["maths"],student1[key_]["science"],student1[key_]["english"]))/3)})
    print("______________________________")

for i in student_list:
    print(i)
    print("_________________________________")

# print(student1["std1"]['name'])
