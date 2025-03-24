bp=int(input("Enter the buying price;"))
sp=int(input("Enter a selling price;"))

if bp>sp:
    print("user is at loss")
elif bp==sp:
    print("The user has no profit or loss")
else:
    print("the user is at a profit")