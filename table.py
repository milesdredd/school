import pandas as pd
a = input("1st category")
b = input("2nd category")
c = input("1st item of list" )
d = input("2nd item of list" )
e = input("3rd item of list" )
f = input()
g = input()
h = input("of")
data = {a:[c,d,e],b:[f,g,h]}
ind=[1,2,3]

table = pd.DataFrame(data,ind)

print(table)
