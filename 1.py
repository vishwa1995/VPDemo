a=eval(raw_input("enter a:"))
b=eval(raw_input("enter b:"))
c=eval(raw_input("enter c:"))
d=eval(raw_input("enter d:"))

if a>1 and a<9:
    ad=a+b+c+d
    print("the addition of number is:")
    print (ad)
     
elif a>9:
    sab=a-b-c-d
    print("the subtraction of number is:")
    print (sab)
elif a>15:
    mul=a*b*c*d
    print("the multiplication of number is:")
    print (mul)
elif a>20:
    di=(a+b)/(c+d)
    print("tne division is:")
    print (di)
else:
    print("invalid")    
    
         

    
    
