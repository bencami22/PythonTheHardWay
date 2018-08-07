from sys import argv
script, file_name = argv

print(f"We are going to erase file:{file_name} \nCTRL+c to cancel, RETURN to proceed")
input()
target=open(file_name, 'w') # w=write, r=read (default), a=append
print("Emptying file")
target.truncate()
print("File emptied!")
to_write_line_1=input(f"Input some text to write to filename {file_name}")
to_write_line_2=input(f"Input some text for another line to filename {file_name}")
target.write(f"{to_write_line_1}\n{to_write_line_2}")
target.close()
