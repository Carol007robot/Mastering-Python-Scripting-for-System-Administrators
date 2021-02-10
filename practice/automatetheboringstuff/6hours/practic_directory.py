from pathlib import Path
import openpyxl
path = Path()
#create a directory
#print(path.mkdir())
#check if the directory exists
#print(path.exists()
#delete the directory
#print(path.rmdir())
#list all the files *.*.
for file in (path.glob('*.py')):
    print(file)