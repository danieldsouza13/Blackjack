test_list = ['gfg', 'i', 's', 'be', 's', 't']

# printing original list
print("The original list is : " + str(test_list))

# using list comprehension
# to convert list of string and characters
# to list of characters
res = [i for jk in test_list for i in jk]

# printing result
print("The list after conversion is : " + str(res))