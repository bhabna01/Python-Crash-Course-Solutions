buffet=('salad','rice','curry','desserts','beef')
for food in buffet:
    print(food)

# buffet[0]='chocolate' modifying tuple can't be done
buffet=('salad','rice','curry','drinks','chicken')
print("Modified Menu:")
for food in buffet:
    print(food)