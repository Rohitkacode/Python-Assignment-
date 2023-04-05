students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
my_dict= {}
#using loop method
for (key, value) in zip(students, subjects):
    my_dict[key] =value 

print(my_dict)
# using dec comprehension

my_dict2 = {key:value for (key, value) in zip(students, subjects)}


