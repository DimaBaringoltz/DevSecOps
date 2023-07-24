import os
import hashlib


def init_all_data():
    all_data = {}
    all_data["BiggestF"] = []
    all_data["BiggestD"] = []
    all_data["All_hash"] = {}
    return all_data


def user_get_file_size(full_path, all_data):
    st = os.stat(full_path)
    temp_size = st.st_size
    file_name = os.path.basename(full_path)
    handle_file(temp_size, file_name, all_data)
    hash_check(full_path, all_data)
    # all_data["BiggestF"].append(temp_size)
#    print(all_data["BiggestF"])
    # print(full_path + "size is " + str(temp_size))


def handle_file(size, file_name, all_data):
    file_info = {"file size": size, "filename": file_name}
    save_info(file_info, all_data)


def save_info(info, all_data):
    all_data["BiggestF"].append(info)


def user_data_dir_size(dirpath, all_data):
    a = dirpath
    size = 0
    for ele in os.scandir(a):
        # size += os.path.getsize(ele)
        size += ele.stat().st_size
    user_handle_dir(dirpath, size, all_data)
    # all_data["BiggestD"].append(dirpath)


def user_handle_dir(dirpath, size, all_data):
    dir_info = {"dir name": dirpath, "dir size": size}
    if dir_info not in all_data["BiggestD"]:
        save_dir_info(dir_info, all_data)


def save_dir_info(info, all_data):
    all_data["BiggestD"].append(info)


def hash_check(full_path, all_data):
    m = hashlib.sha256()
    file_s = full_path
    file_name = os.path.basename(full_path)
    f1 = open(file_s, 'rb')
    temp = f1.read()
    m.update(temp)
    file_hash = m.hexdigest()
    hash_handle(file_name, file_hash, all_data)


def hash_handle(file_name, file_hash, all_data):
    if file_hash not in all_data:
        all_data["All_hash"][file_hash] = file_name
    else:
        print("Duplicate")
