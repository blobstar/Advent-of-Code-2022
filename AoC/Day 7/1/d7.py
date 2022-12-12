import gc
input = "$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k"
#print(input)

log = input.strip().split("\n")
print(log)

class Dir:
    def __init__(self, name: str, parent_dir: object, child_dir: dict, file_sizes: list) -> None:
        self.name: str = name
        self.parent_dir: Dir = parent_dir # only god knows if this will work
        self.child_dir: dict = child_dir
        self.file_sizes: list = file_sizes

def main():
    rootDir = None
    currentDir = None # this is an empty object for now
    print(type(currentDir))
    for com in log:
        snippet = com.strip().split(' ')
        print(snippet)

        if snippet[2] == "/":
            rootDir = Dir(name = snippet[2], parent_dir=None, child_dir={}, file_sizes=[])

        if snippet[0] == "dir":
            newDir = Dir(name = snippet[1], parent_dir = currentDir, child_dir = {}, file_sizes = [])
            print(newDir)
            print("1")
            currentDir.child_dir[snippet[1]] = newDir
            print(type(currentDir.child_dir[com[4:]]))
        if com[0:4] == "$ cd":
            currentDir = com[4:]
            #print(currentDir)
            #newDir = Dir(currentDir, Dir, {}, [])


main()









