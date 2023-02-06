'''Hard drive benchmark 1 (reference time: 250 seconds)
Read a whole file of 109 bytes, 100 bytes each time
Write 109 bytes to a file, 100 bytes each time '''

import time 

start_time = time.time()

#writing first
with open('large_file.txt','wb') as fp: #writing in a binary file 
    for i in range(10**9):
        fp.write(b'a'*100)

# reading 
with open('large_file.txt','rb') as fp:
    for i in range(10**9):
        reading_bytes = fp.read(100)

end_time = time.time()
total_time_taken = end_time -start_time 

print('Total time taken is ', total_time_taken)
