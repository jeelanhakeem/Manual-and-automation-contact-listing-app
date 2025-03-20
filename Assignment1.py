import os
'''
root_path = 'C:\\Users\\HMD Jeelan\\PycharmProjects\\First _program_Project\\PYTHON_PRACTICE'

list = ['datatypes_practice', 'loop_practice', 'file_operation_practice', 'exception_handling_pract']

for items in list:
	path = os.path.join(root_path, items)
	os.mkdir(path)

os.chdir('PYTHON_PRACTICE/datatypes_practice')
print(os.getcwd())
#file1=open('integers.py','w')
file2=open('string.py','w')

os.chdir('PYTHON_PRACTICE/exception_handling_pract')
#print(os.getcwd())
file1=open('exception handling.py','w')

os.chdir('PYTHON_PRACTICE/file_operation_practice')
#print(os.getcwd())
file1=open('file operation.py','w')

os.chdir('PYTHON_PRACTICE/loop_practice')
#print(os.getcwd())
file1=open('loop.py','w')

'''

import os
for a, b, c in os.walk("."):
    for file in c:
        if "python" in file:
            print(file)
