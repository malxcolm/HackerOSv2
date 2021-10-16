import time
from tqdm import tqdm
import os 
#Start Of The Setup

print("HackerOS v2")
print("Version 2.00...")

#Loading with spice
for i in tqdm (range (101), 
               desc="Loading…", 
               ascii=False, ncols=75):
    time.sleep(0.01)
      
print("Complete.")
