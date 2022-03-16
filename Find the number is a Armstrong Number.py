#Find the number is a Armstrong Number
a=int(input("Enter a number"))
n=0
b=a
c=a
while(b>=1):
  #n+=1
  b=b//10
  n+=1
print(n)
sum=0
while(a>=1):
  i=a%10
  
  sum+=pow(i,n)
  a=a//10
print(sum==c)   
