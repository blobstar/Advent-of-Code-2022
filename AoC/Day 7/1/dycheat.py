import gc

class Directory():
    def __init__(self, name: str, super_dir: object, sub_dir: dict, file_sizes: list) -> None:
        self.name : str = name
        self.super_dir : Directory = super_dir
        self.sub_dir : dict= sub_dir
        self.file_sizes : list = file_sizes

    def get_full_dir_size(self):
        # returns the total file size of this directory combined with all subdirectories (recursive)
        child_file_sizes = []
        for item in self.sub_dir.values():
            child_file_sizes.append(item.get_full_dir_size())

        if child_file_sizes:
            return sum(child_file_sizes) + sum(self.file_sizes)
        else:
            return sum(self.file_sizes)

    def get_dir_dict(self):
        # returns a dictionary structure of all the sub directories and their subdirectories (recursive)
        dir_dict = {}
        for item in self.sub_dir.values():
            dir_dict[item.name] = item.get_dir_dict()
        return dir_dict

def main():
    root_dir = None

    # build directory
    with open('input.txt') as file:
        lines = file.readlines()

    current_dir_class = None
    for line in lines:
        snippet = line.strip().split(' ')

        if snippet[0] == 'dir':
            new_dir = Directory(name=snippet[1], super_dir=current_dir_class, sub_dir={}, file_sizes=[])
            current_dir_class.sub_dir[snippet[1]] = new_dir
            continue
        elif snippet[0].isdigit():
            current_dir_class.file_sizes.append(int(snippet[0]))
            continue
        elif snippet[0] != '$' or snippet[1] != 'cd':
            continue

        if snippet[2] == '/':
            root_dir = Directory(name='root', super_dir=None, sub_dir={}, file_sizes=[])
            current_dir_class = root_dir
        elif snippet[2] == '..':
            current_dir_class = current_dir_class.super_dir
        elif snippet[1] == 'cd':
            current_dir_class = current_dir_class.sub_dir[snippet[2]]
    
    # get all directories less than 100000 in size
    dir_size_list = []
    for dir in gc.get_objects():
        if not isinstance(dir, Directory):
            continue

        size = dir.get_full_dir_size()
        if size < 100000:
            dir_size_list.append((dir.name, size))

    print(f"Part 1: {sum([tup[1] for tup in dir_size_list])}")

    # get smallest dir large enough make up needed space when deleted

    contender = root_dir.get_full_dir_size() + 1
    min_size = -(70000000 - contender - 1 - 30000000)

    for dir in gc.get_objects():
        if not isinstance(dir, Directory):
            continue

        size = dir.get_full_dir_size()
        if min_size <= size < contender:
            contender = size

    print(f"Part 2: {contender}")

def get_expected_root_size():
    # Used for debugging the root Directory object to ensure that all the sub Directories are assigned correctly
    
    with open('./day7/data_management.txt') as file:
        lines = file.readlines()

    tracker = 0
    for line in lines:
        snippet = line.strip().split(' ')

        if not snippet[0].isdigit():
            continue

        tracker += int(snippet[0])
    print(tracker)

main()
# get_expected_root_size()