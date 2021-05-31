import os

count = 0
path = input("Enter the directory path where you need to rename: ")
for filename in os.listdir(path):
    filename_without_ext = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1]
    new_file_name = filename_without_ext.replace(
        filename_without_ext, str(count))
    new_file_name_with_ext = new_file_name+extension
    count += 1
    print(new_file_name_with_ext)
    os.rename(os.path.join(path, filename),
              os.path.join(path, new_file_name_with_ext))
