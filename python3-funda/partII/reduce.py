from functools import reduce
a = [1,2,3,4,5]

reduce(lambda x,y:x+y, a) # 15

list(map(lambda x:x*2, a)) # [2,4,6,8,10]
list(filter(lambda x:x*2 > 5, a)) # [3,4]