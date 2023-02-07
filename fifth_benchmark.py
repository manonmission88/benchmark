''' 
Hard drive benchmark 2 (reference time: 10 seconds)
Read a whole file of 10**9 bytes, 10000 bytes each time
Write 10**9 bytes to a file, 10000 bytes each time '''

import time 

start_time = time.time()

#writing first
with open('new_large_file.txt','wb') as fp: 
    bytes_write = 0
    while bytes_write < 10**9:
        chunk = b"0" * 1000
        fp.write(chunk[:min(10**9 - bytes_write, 1000)])
        bytes_write += len(chunk)
    

# reading 
with open('new_large_file.txt', "rb") as f:
    bytes_read = 0
    while bytes_read < 10**9:
        chunk = f.read(1000)
        bytes_read += len(chunk)

end_time = time.time()
total_time_taken = end_time -start_time 

print('Total time taken is ', total_time_taken)