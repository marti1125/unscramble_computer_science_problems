"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def get_unique_number(arr):
    unique_numbers = []
    for ar in arr:
        if ar[0] not in unique_numbers:
            unique_numbers.append(ar[0])
        if ar[1] not in unique_numbers:
            unique_numbers.append(ar[1])
    return unique_numbers


def task1():
    texts_unique_numbers = get_unique_number(texts)
    calls_unique_numbers = get_unique_number(calls)

    count = len(texts_unique_numbers + texts_unique_numbers)

    print(f"There are {count} different telephone numbers in the records.")

if __name__ == "__main__":
    task1()
