cube=[value**3 for value in range(1,11)]
print('The first three items are:')
for number in cube[:3]:
    print(number)
print('the middle three items are:')
for number in cube[3:6]:
    print(number)
print('The last three items are:')
for number in cube[6:9]:
    print(number)