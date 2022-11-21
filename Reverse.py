from builtins import print

values=[1,2,"mahesh",3,4]
print(values)
print(values[0])
print(values[1:4])
values.insert(3,"konanti")
print(values)
values.append("TESTER")
print(values)

#tuple its immutable we cant update
a=(1,2,4,5,)
print(a[1])

#dictionary
a={1:"mahesh",9:"abhishek",3:"shubham"}
a[9]="rahul"
print(a)

#empty dictionary
b={}
b["firstname"]="mahesh"
b["lastname"]="shubham"
print(b)


txt="mahesh timappa konanti"
print(txt[1:5])


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
