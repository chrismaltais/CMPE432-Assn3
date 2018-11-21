with open("error_log.txt", "r") as source:
    lines = [line for line in source]
	
import time	
import random
import os
 
if os.path.exists("./netIDs_log.txt"):
  os.remove("./netIDs_log.txt")
else:
 print("The file does not exist, creating new fresh log") 

t_end = time.time() + 60 * 30 # 30 minutes


while time.time() < t_end:
    random_choice = random.sample(lines, 1)
    time.sleep(3) 
    with open("./netIDs_log.txt", "a") as sink:
      sink.write("".join(random_choice))	