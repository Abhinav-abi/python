#Print Armstrong number between 1 to 999
ar=[]
for a in range(1,1000):
  c=a
  sum=0
  while(a>=1):
    i=a%10
  
    sum+=pow(i,3)
    a=a//10
  if(sum==c):
    ar.append(c)  
print(ar)
