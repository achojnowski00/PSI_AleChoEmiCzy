a_list = [1,2,3,4,5,6]
b_list = [7,4,9,23,2]
c_list = []

for ind,val in enumerate(a_list):
    if ind%2==0:
        c_list.append(val)

for ind,val in enumerate(b_list):
    if ind%2!=0:
        c_list.append(val)

print(c_list)