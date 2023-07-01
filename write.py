import os
# w-> is used to delete any existing content and write new one
# a-> is used to append an existing content
file=open('layton2.txt','w')
file.write('hello layton matheka')
file.close()

# another way of doing that
with open('layton2.txt','w') as f:
    f.write('hello layton matheka')