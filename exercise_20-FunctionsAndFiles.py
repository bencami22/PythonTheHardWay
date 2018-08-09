from sys import argv
script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(f):
    print(f"{f.readline()}", end = "")

current_file=open(input_file)
print("Printing whole file:")
print_all(current_file)

print("Rewind to the beginning...")
rewind(current_file)

print("Printing a line")

print_a_line(current_file)
