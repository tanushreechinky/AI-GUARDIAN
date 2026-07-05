totalmark=int(input("enter the total mark obtained out of 600 "))
percentage=(totalmark/600)*100
print("percentage",percentage)
if percentage>30 and percentage<=50:
    print("3rd division")
elif percentage>50 and percentage<=60:
    print("2nd division")
elif percentage>60 and percentage<=100:
    print("1st division")
else:
    print("fail")