with open('Day 3\/1\input.txt') as f:
    pallet = f.readlines()
f.close

# first thing we need to do is split each rucksack into compartments
print(pallet)
splitsack = []
def pallet_splitter(pallet):
    for rucksack in pallet:
        ruckie1 = []
        ruckie2 = []
        ruckieCol = []
        for i in range(len(rucksack)-1):
            if i < ((len(rucksack)-1)/2):
                ruckie1.append(rucksack[i])
                #print(rucksack[i])
            else:
                ruckie2.append(rucksack[i])
            i+=1
        ruckieCol.append(ruckie1)
        #print(ruckieCol)
        ruckieCol.append(ruckie2)
        splitsack.append(ruckieCol)
        print(splitsack)
    return splitsack
pallet_splitter(pallet)

