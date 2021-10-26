## zadanie 6
list = [1,2,3,4,5,6,7,8,9,10]
listnew = list[5:]
list = list[:5]
print(list, listnew)

## zadanie 7

join = list+listnew
join.insert(0,0)
copy = join 
join.sort(reverse=True)
print(join)

