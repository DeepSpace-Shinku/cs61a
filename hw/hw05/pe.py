import math
while True:
    distance = float(input())
    pace_min, pace_sec = int(input()), int(input())
    time_min, time_sec = pace_min * distance, pace_sec * distance
    time_min, time_sec = math.floor(time_min), time_sec + (time_min - math.floor(time_min)) * 60
    while time_sec >= 60:
        time_sec -= 60
        time_min += 1
    print(time_min, int(time_sec))