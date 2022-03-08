#Add 10 numbers using array
i=0
a=[]
for i in range(0,10):
  b=int(input("enter anumber"))
  a.append(b)
print(a)
sum=0
for i in range(0,10):
  sum+=a[i]
print("sum of 10 numbers is",sum)
