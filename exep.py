try:
    age = int(input("enter age: "))
    income = 2000
    cost = 2000/age
    print(cost)
except ZeroDivisionError:
    print("age could not be zero")
except ValueError:
    print("invalid value")