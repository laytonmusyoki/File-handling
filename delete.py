import os

if os.path.exists('lay.txt'):
    os.remove('lay.txt')
    print('file deleted successfully')
else:
    print('File does not exist')



# deletting a folder
# use  os.rmdir()  command