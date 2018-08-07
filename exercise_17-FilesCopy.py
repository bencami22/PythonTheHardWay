from sys import argv
from os.path import exists
script, file_name_in, file_name_out = argv

print(f"Copying from {file_name_in} to {file_name_out}")

file_in = open(file_name_in)
txt_to_copy=file_in.read()

print(f"Size of file: {len(txt_to_copy)} bytes")
print(f"File name out already exists- {exists(file_name_out)}")

file_out = open(file_name_out, "w")
file_out.write(txt_to_copy)

print("Copied successfully")

file_in.close()
file_out.close()
