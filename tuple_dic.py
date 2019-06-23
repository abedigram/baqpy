
tuple = (1,2,3) #could not be modified
# print(tuple[0])


coordinates = (1,2,3)  #even works on lists
x, y, z = coordinates

print(x)
print(y)
print(z)

# dictionaries

customer = {   #keys would be unique
    "name": "MohammadBagher",
    "age": 21,
    "is_verified": True
}

customer["birthdate"] = "nov 1997"

print(customer["name"])
print(customer.get("naaaame", "mr ghazi")) #does not make error if not available
# can return a default value -> mr ghazi

print(customer.get("birthdate"))