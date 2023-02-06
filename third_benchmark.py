'''Memory benchmark (reference time: 100 seconds)
Read from 5 × 109 different array elements, 4 bytes each time
Write to 5 × 109 different array elements, 4 bytes each time '''

import time 

start_time = time.time()
#creating the array 
array_elements = [0] * (5*10**9)

#reading and writing 
for i in range(5*10**9):
    array_elements[i] = i 
    another_array = array_elements[i]

end_time = time.time()
total_time_taken = end_time -start_time 

print('Total time taken is ', total_time_taken )



