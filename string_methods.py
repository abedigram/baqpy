course = 'wowww wE codE iN pYthon!'
print(len(course))
print(course.upper()) # just copy, make result and print
print(course.lower()) # does not change the source
print(course)

print(course.find('p'))
print(course.find('codE'))  # first index occurance
print(course.replace('codE','code and debug'))
print(course.replace('w','d')) # replace all occurences
print(course)

print('wE' in course) # true false expression
print('we' in course)

print(course.title()) # capital first chars