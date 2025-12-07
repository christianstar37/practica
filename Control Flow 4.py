n_month = int(input("What is the number of the current month? "))

if n_month <= 3:
    print("Winter!")
elif n_month <= 6:
    print("Spring!") 
elif n_month <= 9:
    print("Summer!")
elif n_month <= 12:
    print("Autumn!")  
else:
    print("Invalid")