'''64-bit Floating point operation benchmark (reference time: 100 seconds)
Same as integer, use double precision floating point numbers instead of integer.
--•10^10 additions 
•5 × 10^9 multiplication 
•2 × 10^9 division '''
import time 

start_time = time.time()
initial_value = 1.0
# for addition 
for i in range(10**10):
    initial_value += i
#for multiplication 
for i in range(5*10**9):
    initial_value *= i
# for division
for i in range(1,2*10**9): # started from 1 to avoid zero division error 
    initial_value /= i

end_time= time.time()
total_time_taken = end_time -start_time

print('total time taken is ',total_time_taken)


