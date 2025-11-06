a=int(input('Enter a value:'))
b=int(input('Enter b value:'))
c=int(input('Enter c value:'))
if(a>b and a>c):
    if(b>c):
        print(a,b,c)
    else:
        print(a,c,b)
elif(b>a and b>c):
     if(a>c):
         print(b,a,c)
     else:
         print(b,c,a)
else:
     if(a>b):
         print(c,a,b)
     else:
         print(c,b,a)
