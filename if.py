is_hot = True
is_cold = False

if is_hot:
    print("it is a hot day")
    print("drink water")
elif is_cold:
    print("it is a cold day")
else:
    print("enjou ur day")

if is_cold and is_hot:
    print("it's a dizzy day")

if not is_cold and is_hot:
    print("it's a HOT day")

if is_cold or is_hot:
    print("it's a day")

temp = 30

if temp > 30: # == != >=
    print("hot")
else:
    print("not hot")

#loop

i=1

while i<=5:
    print('*' * i)
    i+=1
else:
    print("done")

for item in "Python":
    print(item)

for item in ['mosh', 'john', 'sarah']:
    print(item)

for item in range(5,20,2):
    print(item)

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")