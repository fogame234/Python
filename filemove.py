import os
import shutil
from pathlib import Path
from tkinter import filedialog
from tkinter import *

fileWindow = Tk()
fileWindow.withdraw()
source_folder = Path(filedialog.askdirectory()) 
extension = ['.csv', '.xlsx', '.xls', '.sql']

def get_new_file_name(file_name, duplicate_num):
  # handle degenerate case of 0
  if duplicate_num == 0:
    return file_name

  # Split the path into the file stem and the extension
  # Docs for os.path.splitext: https://docs.python.org/3/library/os.path.html#os.path.splitext
  stem, ext = os.path.splitext(file_name)

  # Concatenate the duplicate num w/ file stem and add ext
  # For example file.txt with duplicate_num of 3 would become file_3.txt
  return stem + "_" + str(duplicate_num) + ext

def move_file(source_folder, dest_folder, file_name, duplicate_num=0):
  new_file_name = get_new_file_name(file_name, duplicate_num)
  if os.path.exists(os.path.join(dest_folder, new_file_name)):
      move_file(source_folder, dest_folder, file_name, duplicate_num + 1)
  else:
      src_file = os.path.join(source_folder, file_name)
      dst_file = os.path.join(dest_folder, new_file_name)
      shutil.move(src_file, dst_file)

for root, dirs, files in os.walk(source_folder):

    for fn in files:
        src_path = Path(root).joinpath(fn)
        rel_path = os.path.relpath(src_path, source_folder)
        if src_path.suffix in extension:
            if '_' in root:
                continue
            else:
                if src_path.suffix == ".sql":
                    dest_folder = r"/path"
                    dest_path = Path(dest_folder).joinpath(rel_path)                    
                if src_path.suffix != ".sql":
                    dest_folder = r"/path"
                    dest_path = Path(dest_folder).joinpath(rel_path) 
                print("Scanning: " + str(src_path))
                if os.path.isfile(src_path):
                    parentDir = Path(src_path).parent
                    isfile = True
                    if isfile and parentDir == source_folder:
                        move_file(root, dest_folder, fn)
                        print("File Moved: " + fn)
                        continue
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                move_file(src_path.parent, dest_path.parent, fn)
                print("File Moved: " + str(src_path))
                if len(os.listdir(src_path.parent)) == 0:
                    os.rmdir(src_path.parent)
                    print("Removed: " + str(src_path.parent))
        else:
            noPassword = (source_folder).joinpath("_NO_PASSWORDS")
            dest_no = (noPassword.joinpath(rel_path))
            if '_' in root:
                continue
            else:
                if os.path.isfile(src_path):
                    parentDir = Path(src_path).parent
                    isfile = True
                    if isfile and parentDir == source_folder:
                        continue
                dest_no.parent.mkdir(parents=True, exist_ok=True)
                move_file(src_path.parent, dest_no.parent, fn)
                print("File Moved: " + str(src_path))
                if len(os.listdir(src_path.parent)) == 0:
                    os.rmdir(src_path.parent)
                    print("Removed: " + str(src_path.parent))
