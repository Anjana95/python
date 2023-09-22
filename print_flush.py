import time

count_sec = 3

for secs in reversed(range(count_sec+1)):
    if secs > 0:
        print(secs,flush=False)
        time.sleep(3)
    else:
        print("Start")

