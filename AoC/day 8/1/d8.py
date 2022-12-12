import array as arr

input = "30373\n25512\n65332\n33549\n35390\n"
input = input.strip()
input = input.split("\n")

for i in range(len(input)):
    input[i] = list(input[i])

def isTreeAlone(forest):
    visible = 0
    for y in range(len(forest)):
        for x in range(len(forest[0])):
            #params
            by = len(forest)
            bx = len(forest[0])

            #lookUpDown
            lookUpArr = []
            lookDownArr = []
            for i in range((by+y)-len(forest)):
                
                lookUpArr.append(int(forest[y-by-1-i][x]))
                
            print(lookUpArr, len(lookUpArr))
    print(visible)

print(input)
isTreeAlone(input)
