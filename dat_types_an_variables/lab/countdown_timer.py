import time
import sys
import winsound

timer_time = int(input("Set timer in minutes: ")) - 1
minutes = timer_time

while minutes >= 0:
    for seconds in range(59, -1, -1):
        current_time = f"{minutes:02d}:{seconds:02d}"
        sys.stdout.write('\r' + current_time)
        time.sleep(1)

    minutes -= 1

n = 1
for _ in range(3):
    sys.stdout.write('\r' + "Time is over" + "!" * n)
    n += 1
    winsound.PlaySound('*', winsound.SND_ALIAS)
