'''Hard drive benchmark 1 (reference time: 250 seconds)
Read a whole file of 10**9 bytes, 100 bytes each time
Write 10**9 bytes to a file, 100 bytes each time '''

import time 

start_time = time.time()

#writing first
with open('large_file.txt','wb') as fp:
    bytes_write= 100 #writing in a binary file 
    while bytes_write < 10**9:
        parts = b'0' * 100
        fp.write(parts[:min(10**9-bytes_write,100)])
        bytes_write += len(parts)


# reading 
with open('large_file.txt','rb') as fp:
    bytes_read = 100
    while bytes_read < 10**9:
        parts = fp.read(100)
        bytes_read += len(parts)

end_time = time.time()
total_time_taken = end_time -start_time 

print('Total time taken is ', total_time_taken)
