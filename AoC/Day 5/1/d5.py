# this reads in the input
with open('input.txt') as f:
    lines = f.read()
f.close

#print(lines)

#make data structures

s1 = ['[B]','[G]','[S]','[C]']
s2 = ['[T]','[M]','[W]','[H]','[J]','[N]','[V]','[G]']
s3 = ['[M]','[Q]','[S]']
s4 = ['[B]','[S]','[L]','[T]','[W]','[N]','[M]']
s5 = ['[J]','[Z]','[F]','[T]','[V]','[G]','[W]','[P]']
s6 = ['[C]','[T]','[B]','[G]','[Q]','[H]','[S]']
s7 = ['[T]','[J]','[P]','[B]','[W]']
s8 = ['[G]','[D]','[C]','[Z]','[F]','[T]','[Q]','[M]']
s9 = ['[N]','[S]','[H]','[B]','[P]','[F]']

r1 = ['[Z]','[N]']
r2 = ['[M]','[C]','[D]']
r3 = ['[P]']

rbigShelf = []
rargs = (r1,r2,r3)
rbigShelf.append(rargs)
rbigShelf = rbigShelf[0]
rinstruction = ['move 1 from 2 to 1','move 3 from 1 to 3','move 2 from 2 to 1','move 1 from 1 to 2']

bigShelf = []
args = (s1,s2,s3,s4,s5,s6,s7,s8,s9)
bigShelf.append(args)
bigShelf = bigShelf[0]
#print(bigShelf)

#print(lines)
radha = lines.split('\n')
radha = radha[10:-1]
#print(radha)

def crane(array,pallets):
    print(pallets)
    
    crate = pallets[array[1]-1][:-(array[0])]
    pallets[array[1]-1] = 
    #print(crate)
    #print(pallets[array[1]-1])
    pallets[array[2]-1].append(crate)
    #print(pallets[array[2]-1])
    print('step',i,pallets)
    return pallets

def parser(instructions):
    
    # crate number to move
    start_crate_count = instructions.find('move') + 5
    end_crate_count = instructions.find('from')
    crate_count = int(instructions[start_crate_count:end_crate_count])

    # start shelf
    start_shelf_index = instructions.find('from') + 5
    end_shelf_index = instructions.find('to')
    start_shelf = int(instructions[start_shelf_index:end_shelf_index])

    # end shelf
    end_shelf_start = instructions.find('to') + 2
    end_shelf = int(instructions[end_shelf_start:len(instructions)])
    
    return [crate_count, start_shelf, end_shelf]
final = []
for instruction in radha:
    print(instruction)
    final = (crane(parser(instruction),bigShelf))
final2 = []
for i in final:
    final2.append(i[len(i)-1])

print('final',final2)

        
