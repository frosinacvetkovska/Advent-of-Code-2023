import csv
import os
import re

def calibrate_first_last_number(file):   
    calibrate_num = []
    replacements_dictionary = {'one' : 'on1e', 'two' : 'tw2o', 'three' : 'thr3e','four': 'fo4ur', 'five':'fi5ve','six': 'si6x','seven': 'sev7en','eight' : 
    'ei8ght','nine':'ni9ne'}
    with open("input.txt", "r") as f:
        for line in f:
            for key,value in replacements_dictionary.items():
                line = line.replace(key, value)
            match = re.findall(r'\d', line)
            if match:
                first_num = str(match[0])
                last_num = str(match[-1])
                calibrate_num.append(first_num + last_num)
    total = sum(int(num) for num in calibrate_num)
    print(f"The calibrate number is: {total}")
    return None

file = 'input.txt'
calibrate_first_last_number(file)



