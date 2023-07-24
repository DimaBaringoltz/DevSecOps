def check_size(all_data):
    top_files = all_data["BiggestF"][:]
    n = min(10, len(top_files))

    for i in range(n):
        max_size = -1
        max_idx = -1

        for j, file_info in enumerate(top_files):
            if file_info['file size'] > max_size:
                max_size = file_info['file size']
                max_idx = j

        if max_idx != -1:
            file_info = top_files.pop(max_idx)
            file_name = file_info['filename']
            file_size = file_info['file size']
            print("file name is ", file_name, "file size is ", file_size)


def check_dir_size(all_data):
    top_dir = all_data["BiggestD"][:]
    n = min(10, len(top_dir))
    for i in range(n):
        max_size = -1
        max_idx = -1
        for j, dir_info in enumerate(top_dir):
            if dir_info['dir size'] > max_size:
                max_size = dir_info['dir size']
                max_idx = j
        if max_idx != -1:
            dir_info = top_dir.pop(max_idx)
            dir_name = dir_info["dir name"]
            dir_size = dir_info['dir size']
            print("dir name is ", dir_name, "dir size is ", dir_size)
