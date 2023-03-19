# In here we are finding the user dish from different menus and tell what type of dish is that

indian = ["Buriyani", "samosa"]
sriLankan = ["milk rice", "string hoppers"]

dish = input("Enter the dish name : ")

if dish in indian:
    print("This is a indian food")
elif dish in sriLankan:
    print("This is a sri lankan food")
else:
    print("Please try another one, this is not in our menu")