x=int(input())
if x<0:
    print("Ture")
elif 0<x<10:
    print("Ture")  
elif x%10==0:  
    print("False")
else:
    y=x
    reversed_x=0
    while y>0 :
        y_end=y%10
        reversed_x=reversed_x*10+y_end
        y=y//10
    if x==reversed_x :
        print("Ture")
    else:
        print("False")
    