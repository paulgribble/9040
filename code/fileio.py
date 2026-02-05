
# write 5 bytes to a file specifying using binary
with open("hello1", "wb") as f:
    f.write(bytes([0b01101000]))
    f.write(bytes([0b01100101]))
    f.write(bytes([0b01101100]))
    f.write(bytes([0b01101100]))
    f.write(bytes([0b01101111]))

# write 5 bytes to a file specifying using hex
with open("hello2", "wb") as f:
    f.write(b"\x68")
    f.write(b"\x65")
    f.write(b"\x6c")
    f.write(b"\x6c")
    f.write(b"\x6f")

# write a 32-bit unsigned integer and an 8-bit unsigned integer to a file
import numpy as np
with open("hello3", "wb") as f:
    np.uint32(1819043176).tofile(f)
    np.uint8(111).tofile(f)

# write 5 ASCII/UTF-8 characters to a file
with open("hello4", "w") as f:
    f.write("hello")

# write 3 lines of ASCII to a file
with open("hello5", "w") as f:
    f.write("hello\n")
    f.write("from\n")
    f.write("paul")

# read all lines from an ASCII file
with open("hello5", "r") as f:
    data = f.read()

with open("hello5", "r") as f:
    data = f.readlines()

with open("hello5", "r") as f:
    data = [l.strip() for l in f]

# read from a .csv file into a numpy array
import numpy as np
data = np.genfromtxt("hello.csv", delimiter=",", skip_header=True)

# read from a .csv file into a pandas data frame
import pandas as pd
data = pd.read_csv("hello.csv")


