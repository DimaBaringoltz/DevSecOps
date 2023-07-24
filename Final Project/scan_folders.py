import os
import data
import report


def main():
    all_data = data.init_all_data()
    list_all_content('D:\DevSecOps\Python\Final Project', all_data)
    report.check_size(all_data)
    report.check_dir_size(all_data)
    # print(all_data)


def list_all_content(dirpath, all_data):
    item_list = get_dir_content(dirpath)
    # all_data = data.init_all_data()
    for item in item_list:
        full_path = os.path.join(dirpath, item)
        if dir_check(dirpath + "/" + item):
            # print("list dir ", item)
            list_all_content(dirpath + "/" + item, all_data)
            data.user_data_dir_size(dirpath, all_data)
        else:
            # print(indent + item)
            data.user_get_file_size(full_path, all_data)

    # report.check_size(all_data)


def get_dir_content(dirpath):
    content = os.listdir(dirpath)
    return (content)


def dir_check(dirpath):
    return os.path.isdir(dirpath)


# list_all_content('D:\DevSecOps\Python\Final Project')
main()
