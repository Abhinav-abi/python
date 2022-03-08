#Sum of series 1 + 1/2 + 1/3 + 1/4 + .... + 1/n
n=int(input("enter the number"))
i=1
sum=0
for i in range(1,n+1):
 print(f'1/{i}',end="+")
for i in range(1,n+1):
  sum=sum+1/i
print("\n sum is",sum)
