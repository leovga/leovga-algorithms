#Name: Eleftherios Vganges
#Date: 10/02/2023
#Purpose: Test the speed of a Selection Sort Algorithm and a Quicksort Algorithm over n from 5 to 200 to test speed at certain values.
#   Finds the crossover point in the doc file and sets it to 19, and develops a hybrid sort around it.

import random as random
import time

#Basic Selection Sort Algorithm - https://www.geeksforgeeks.org/python-program-for-selection-sort/#
def selectionsort(arr, n):
    for i in range(n):
        minimum = i
        for j in range(i+1, n):
            if arr[j] < arr[minimum]:
                minimum = j
        (arr[i], arr[minimum]) = (arr[minimum], arr[i])
    return arr

#Basic Partition that is used both by QuickSort and epv15 Sort - https://www.geeksforgeeks.org/python-program-for-quicksort/
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return i+1

#Basic Quicksort function to find pivot and sort left and right arrays - https://www.geeksforgeeks.org/python-program-for-quicksort/
def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p-1)
        quicksort(arr, p+1, high)

#Altered Selection Sort that takes in a low and high value instead of the overall size of the array
def lhselection(arr, low, high):
    for i in range(low, high):  #only interates through given array size instead of complete n (this caused a major time delay when I didn't catch it)
        minimum = i
        for j in range(i+1, high):
            if arr[j] < arr[minimum]:
                minimum = j
        (arr[i], arr[minimum]) = (arr[minimum], arr[i])
    return arr

#Hybrid Algorithm Developed from a combination of Quicksort and Selection Sort
def epv15sort(arr, low, high):
    while low < high: # while loop so that the taken results can be continuosly compared to 19 to switch over to insertion when required
        if(high - low + 1 <= 19):   # if the lowest and highest value are less than 20, switch to selection
            lhselection(arr, low, high)
            break   # break while loops when beginning insertion
        
        p = partition(arr, low, high)   #gets pivot
        upper = high - p    # finds  the upper and lower difference to compare left and right array sizes
        lower = p - low     
        if upper >= lower:  # calls specific side to be sorted first, and allows it to go down to insertion
            epv15sort(arr, p+1, high)
            high = p-1  # sets next high call to left side of pivot
        elif lower > upper: # these comparisons are necessary or the algorithm enters an infinite loop at n > 19 
            epv15sort(arr, low, p-1)
            low = p + 1 # sets next low call to right side of pivot
        else:
            pass


def main():

    total_time = 0    # initializes total time, which is used for testing

    
    n = int(input("Size of array (n): "))   # gets n 
    check = False
    while check == False: # decision for what algorithm to sort with
        sel = int(input("Sorting Algorithm: 1(Selection), 2(Quicksort), 3(epv15_hybrid) - "))
        if sel < 4 and sel > 0:
            check = True

    arr = []    # initializes an empty array
    for i in range(n):  # for size of n, add a random number between 0 and n to list.
        randnum = random.randint(0, n)  # I chose n because a constant would produce a larger amount of duplicates at a greater n value (100 while n > 200)
        arr.append(randnum) #           and n would be able to produce 1 unique element per integer in n.

    print("Unsorted Array:")    # prints out unsorted array
    print(arr)

    start_time = time.time()    # starts time before selecting sort
    if sel == 1:
        arr = selectionsort(arr, n) # calls basic selection
    elif sel == 2:
        quicksort(arr, 0, n-1)  # calls basic quicksort
    elif sel == 3:
        epv15sort(arr, 0, n-1)   # calls epv15 sort

    total_time = time.time() - start_time   # subtracts starting time from current time to find length of time taken to sort
    print("Sorted Array:")  # prints array and time
    print(arr)
    print("Time Taken: ", total_time)


    # Code for testing, similar to above but runs an algorithm for 100 loops and finds the average length of time.
    '''
    for i in range(100):
        arr = []
        for i in range(n):
            randnum = random.randint(0,100)
            arr.append(randnum)

        start_time = time.time()       
        if sel == 1:
            arr = selectionsort(arr, n)
        elif sel == 2:
            quicksort(arr, 0, n-1)
        elif sel == 3:
            epv15sort(arr, 0, n-1)

        total_time = total_time + (time.time() - start_time)

    print(total_time / 100)
    '''

main()