
 # ***************** 01.series calculator (simple calculations) ****************

import math as m

series = input()
seasons = int(input())
episodes = int(input())
series_time = float(input())

ads_time = series_time * 0.20
extra_time = (seasons * 10)
total_time = m.floor(seasons * episodes * (series_time + ads_time) + extra_time)

print(f"Total time needed to watch the {series} series is {total_time} minutes.")
