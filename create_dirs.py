"""create a sequence of directories"""
import os

def create_dir(start, end):
    for i in range(start, end + 1):
        dir_name = "day_" + str(i).rjust(3, "0")
        print("creating directory: " + dir_name)
        new_dir = os.path.join(os.getcwd(), dir_name + "/resources")
        try:
            if not os.path.isdir(new_dir):
                os.makedirs(new_dir)
        except FileExistsError:
            print("directory already exists")

if __name__ == "__main__":
    try:
        start = int(input("Enter the starting number: "))
    except:
        start = 1
    try:
        end = int(input("Enter the ending number: "))
    except:
        end = 100
    create_dir(start, end)
