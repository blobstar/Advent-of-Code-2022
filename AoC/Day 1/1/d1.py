with open('Day 1\/1\input.txt') as f:
    lines = f.readlines()
    f.close

print(lines)
elf_food_list = []
basket = 0
for food in lines:
    if food != '\n':
        basket += int(food.strip())
        #print('ping')
    else:
        elf_food_list.append(int(basket))
        basket = 0
print(elf_food_list)

biggestParcel = 0 
for parcel in elf_food_list:
    if parcel > biggestParcel:
        biggestParcel = parcel

elf_food_list.sort(reverse = True)
top3 = sum(elf_food_list[:3])
print(top3)
print(elf_food_list[:3])
print(biggestParcel)
#print(top3)

