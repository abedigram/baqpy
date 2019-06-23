def greet_user():
    print("heyyyyyy")
    print("thereeee")


# print("welcome")
# greet_user()

def greet_name(name, last):
    print(f"hi {name} {last}!")

greet_name("john", "smith")
greet_name(last="smith", name="john")
greet_name("john", last="smith")


def square(num):
    return num * num

print(square(3))