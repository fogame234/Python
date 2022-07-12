import time
import os

finalStart = time.perf_counter()
source_folder = r"C:/Users/Trevor/Documents/VeriCloud/Test/"
def _count_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)

lineCount = int(0)

for file in os.listdir(source_folder):
    start = time.perf_counter()
    with open(source_folder + file, 'rb') as fp:
        c_generator = _count_generator(fp.raw.read)
        # count each \n
        count = sum(buffer.count(b'\n') for buffer in c_generator)
        print('Total lines:', count + 1)
    stop = time.perf_counter()   
    print(file + " Start: " + str(start))
    print(file + " Stop: " + str(stop))   
    fileTime = float(stop - start)
    print("File time: " + str(fileTime)+ "\n")
    lineCount += count

finalStop = time.perf_counter()  

final = float(finalStop - finalStart)
print(final)
print("Final line count:" + str(lineCount))