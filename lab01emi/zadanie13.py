students = [
    {"name":"Emilia", "age":22, "school":"UWM"},
    {"name":"Jakub", "age":23, "school":"WSB Gdańsk"},
    {"name":"Adrian", "age":22, "school":"PG"}
]
data = ""
count = 1
for item in students:
    data+="student nr.{}: student's name: {}, student's age: {}, student's school: {}\n".format(count,item["name"],item["age"],item["school"])
    count+=1

print(data)