import re

class dir:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.child_dirs: list[dir] = []
        self.child_files = []
        self.parent = parent
        
    def __gt__(self, other: dir):
        return self.get_size() > other.get_size()
    def __ge__(self, other: dir):
        return self.get_size() >= other.get_size()
    def __lt__(self, other: dir):
        return self.get_size() < other.get_size()
    def __le__(self, other: dir):
        return self.get_size() <= other.get_size()
        
    def add_dir(self, child):
        self.child_dirs.append(child)
    def add_file(self, file):
        self.child_files.append(file)
    def get_size(self):
        sum_ = 0
        for child in self.child_dirs:
            sum_ += child.get_size()
        sum_ += sum(self.child_files)
        return sum_

with open('input/puzzle 7', 'r') as f:
    dirs = []
    s = f.read().split('\n')
    root = dir(name='/', parent=None)
    current_dir: dir = root
    dirs.append(root)
    cd = re.compile(r"[$] cd (\w+)")
    file_re = re.compile(r"([0-9]+) (\w+)")
    for line in s:
        if re.search(r"[$] cd \.\.", line):
            current_dir = current_dir.parent
        elif re.search(cd, line) != None:
            m = re.search(cd, line)
            child = dir(name=m.group(1), parent=current_dir)
            dirs.append(child)
            current_dir.add_dir(child=child)
            current_dir = child
        elif re.search(file_re, line) != None:
            m = re.search(file_re, line)
            current_dir.add_file(int(m.group(1)))
        elif re.search(r"[$] cd \\", line):
            current_dir = root
    
    total = 0
    for directory in dirs:
        size = directory.get_size()
        if size <= 100000:
            total += size            
    print(total)
    
    required_space = 30000000 - (70000000 - root.get_size())
    dirs = sorted(dirs)
    
    for i in dirs:
        if i.get_size() >= required_space:
            print(i.get_size())
            break
    
    
    