'''Memory benchmark (reference time: 100 seconds)
Read from 5 × 109 different array elements, 4 bytes each time
Write to 5 × 109 different array elements, 4 bytes each time '''

import time 

start_time = time.time()
#creating the array 
array_elements = [None] * (5*10**5)

#reading and writin
for i in range(10**4):
    for j in range(5*10**5):
        array_elements[j] = j 
        another_array = array_elements[j]

end_time = time.time()
total_time_taken = end_time -start_time 

print('Total time taken is ', total_time_taken )



