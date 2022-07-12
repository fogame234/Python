import natsort
import os

source_folder = r"C:/Users/Trevor/Documents/VeriCloud/Test/"
dest_folder = r"C:/Users/Trevor/Documents/VeriCloud/Test/"

count = int(1)
for file in natsort.os_sorted(os.listdir(source_folder)):
    new = source_folder + str(count) + "_Combolist" + ".txt"
    if file not in new:
        with open(file, 'r', encoding="utf_8") as reader:
            # Note: readlines doesn't trim the line endings
            dog_breeds = reader.readlines()


        with open(dest_folder + str(count) + "_Combolist.txt", 'a', encoding="utf_8") as fp:
            for line in (dog_breeds):
                if line.__contains__(":") and not line.__contains__("http"):
                    fp.write(line)
                else:
                    continue
        os.remove(source_folder + file) 
    count += 1