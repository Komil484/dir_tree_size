import os


def bytes_to_units(size):
    if size > 1024 ** 3:
        return f"{size / 1024 ** 3:.2f} GB"
    if size > 1024 ** 2:
        return f"{size / 1024 ** 2:.2f} MB"
    if size > 1024:
        return f"{size / 1024:.2f} KB"
    return f"{size:.2f} Bytes"


class TreeNode:
    def __init__(self, path: str, parent_full_path=None):
        self.path = path
        self.full_path = parent_full_path + "\\" + path if parent_full_path else path
        self.isdir = os.path.isdir(self.full_path)
        if self.isdir:
            child_paths = sorted(os.listdir(self.full_path),
                                 key=lambda _path: 1 if os.path.isdir(self.full_path + "\\" + _path) else 0)
            self.children = [TreeNode(_path, self.full_path) for _path in child_paths]

            self.size = sum([child.size for child in self.children])
        else:
            self.size = os.stat(self.full_path).st_size

    def __str__(self):
        string = ("=" if self.isdir else "-") + " " + self.path + "   " + bytes_to_units(self.size)
        if self.isdir:
            for child in self.children:
                if child.isdir:
                    str_bldr = ["\n " if c == "\n" else c for c in str(child)]
                    string += "\n " + "".join(str_bldr)
                else:
                    string += "\n " + str(child)
        return string


path = input("Input directory path\n")

tree = TreeNode(path)

print(tree)
