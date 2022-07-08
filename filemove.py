import os
import shutil
from pathlib import Path
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
source_folder = filedialog.askdirectory()
#source_folder = Path(r'C:/Users/Trevor/Documents/VeriCloud/')
dest_folder = ""
extension = ""

def fileChoice(dest_folder, extension):
    choice = input("Moving CSV or SQL files? ")

    if choice == "csv":
        root = Tk()
        root.withdraw()
        dest_folder = filedialog.askdirectory()        
        extension = '.csv'

    if choice == "sql":
        root = Tk()
        root.withdraw()
        dest_folder = filedialog.askdirectory()   
        extension = '.sql'

    return dest_folder, extension

dest_folder, extension = fileChoice(dest_folder, extension)

for root, dirs, files in os.walk(source_folder):
    for fn in files:
        src_path = Path(root).joinpath(fn)
        dest_path = dest_folder.joinpath(src_path.name)
        if src_path.suffix == extension:
            if '_' in root:
                continue
            else:
                if os.path.isfile(src_path):
                    parentDir = Path(src_path).parent
                    isfile = True
                    if isfile and parentDir == source_folder:
                        shutil.move(str(src_path), str(dest_folder))
                        print("File Moved: " + fn)
                        continue
                if not os.path.exists(root):
                    print("File already moved: " + fn)
                    continue
                if not dest_path.exists():
                    shutil.move(str(root), str(dest_folder))
                    print("File Moved: " + fn)



