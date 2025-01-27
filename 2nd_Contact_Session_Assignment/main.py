
import re
import os

# 1. logic that prints out my name from the txt fine.

with open('name.txt', 'r') as f:
    line = f.readlines()
    print(line[0])

# 2.  print my current path
path = os.getcwd()
print(path)

# Extraction of Baby Names from html files using Regex
def getbabyname(babyname:str)->None:
    with open('baby2008.html', 'r') as f:
        while True:
            line = f.readline()
            check = re.search(pattern=rf'\b{babyname}\b', string=line, flags=re.IGNORECASE)
            if check != None:
                # print(line)
                # print(check.group())
                print(f'name:{babyname} was found in line:{line}')
                break
    
# getbabyname('Mike')



# Binary Search Implementation
# fine baby name with binary search


#  get the contents of the htmk file, format and sort it
def get_names_list()->list:
    lines = []
    cleaned_lines = []
    with open('baby2008.html','r') as f :
        lines = f.readlines()
        cleaned_lines = [re.sub(
            r'<[^<]+?>|\n|\d+|&nbsp;|[?<>]|(\bform\b|\baction\b|\bimg\b|\bwidth\b)', '', line) for line in lines]
    li =[]
    for i in range(len(cleaned_lines)):
        if cleaned_lines[i] != '' and cleaned_lines[i] != ' ' and cleaned_lines[i] != '\n':
            # print(cleaned_lines[i].strip())
            li.append(cleaned_lines[i].strip())
            
    cleaned_lines = []
    for i in range(32,1031):
        cleaned_lines.append(li[i])
    cleaned_lines.sort()
    return cleaned_lines



# Binary Search Implementation
def binary_search(arr, x)->int:
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # x is present at mid
        else:
            return mid

    # Element is not present in array
    return -1

# Using binary search to search for a name in the list
names = get_names_list()
print(names)
search = binary_search(names, "LondonSimone")
if search != -1:
    print(f"Element is present at index {search}")
else:
    print("Element is not present in array")



    # Implementing a simple bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
