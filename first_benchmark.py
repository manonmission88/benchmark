'''32-bit Integer operation benchmark (reference time: 100 seconds)
•10^10 additions (of integer constants)
•5 × 10^9 multiplication (of integer constants)
•2 × 10^9 division (of integer constants) '''

import time

start_time = time.time()
initial_value = 0
# for addition 
for i in range(10**10):
    initial_value += i
#for multiplictaion 
for i in range(5*10**9):
    initial_value *= i 



