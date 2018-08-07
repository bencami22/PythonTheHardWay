from sys import argv

script, file_name=argv

txt=open(file_name)
print("Filename:", file_name)
print("Content:", txt.read())
txt.close()
