import os
import natsort

source_folder = r"C:/Users/Trevor/Documents/VeriCloud/Test/"

count = int(1)

for file in natsort.os_sorted(os.listdir(source_folder)):
    org = source_folder + file
    new = source_folder + str(count) + "_Combolist" + ".txt"
    if file in new:
        print(file)
        print(org)
        count += 1
        continue
    else:
        os.rename(org, new)
        count += 1

