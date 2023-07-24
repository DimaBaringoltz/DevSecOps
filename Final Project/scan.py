import os


def scaner_file():
    all_schema = []
    all_schema_dir = []
    x = r'D:\DevSecOps\Python\Final Project'
    for root, dir, file in os.walk(x):
        for i in file:
            all_schema.append(os.path.join(root, i))
            all_schema_dir.append(dir)
    return (all_schema, all_schema_dir)


def scaner_dir():
    all_schema_dir = []
    fp = []
    x = r'D:\DevSecOps\Python\Final Project'
    for dirpath, dirnames, filenames in os.walk(x):
        for f in filenames:
            fp.append(os.path.join(dirpath, f))

    return (fp)


print(scaner_dir)


# print(scaner_file())
