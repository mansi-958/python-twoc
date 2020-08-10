a=int(input("Enter the number: "))
b=int(input("Enter the other number: "))
if a<b:
  num=a
else:
  num=b
for i in range(1,num+1):
  if a%i==b%i==0:
    print(i)
