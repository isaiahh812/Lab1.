#Isaiah Hernandez
import os
import random




def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):

    dir_list, file_list = get_dirs_and_files(path)
        
    cat_list = []
    dog_list = []

    # Your code goes here
    for i in range(len(file_list)):
        if((classify_pic(path + '/' + file_list[i])) > 0.5):
            dog_list.append(path + '/' + file_list[i])
        else:
            cat_list.append(path + '/' + file_list[i])
    #Base case
    if dir_list is None:
        return cat_list, dog_list
    #Used in order to have the it look through all directories
    for n in range(len(dir_list)):
        cat, dog = process_dir(path + '/' + dir_list[n])
        cat_list.append(cat)
        dog_list.append(dog)
    return cat_list, dog_list


def main():
    start_path = './'
    print("List of all the cats")
    cat, dog = (process_dir(start_path))
    print(cat)
    print("List of all the dogs")
    print(dog)
main()
    
