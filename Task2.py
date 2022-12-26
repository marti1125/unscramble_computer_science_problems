"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def task2():
    # check if the call is in September and 2026
    sep_2016_calls = [c for c in calls if "09-2016" in c[2]]
    sorter = lambda x : [int(x[3]), x[2], x[1], x[0]]
    sorted_calls = sorted(sep_2016_calls, key=sorter)
    hight_time = sorted_calls[-1]
    print(f"{hight_time[0]} spent the longest time, {hight_time[3]} seconds, on the phone during September 2016.")


if __name__ == "__main__":
    task2()
