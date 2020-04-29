'''
Given n elements in an array, find the majority element which strictly repeats more than
half the time

In this algorithm 
    1. assume a majority element and intialize the counter to 1. 
    2. scan through the array and at each point if the new element matches our current guess 
       we increment the counter, otherwise we decrement it.
    3. if the counter is zero, then we take the next element as our guess and we change the
       counter to 1 again
    4. check if the guessed element is the majority element which strictly repeats more than half
    5. If it does, print that element or else there is no majority element in the given array

for example 
Input: A = [9, 9, 4, 5, 9, 9, 6, 9]

here the number 9 is the majority element as it appears 5 times in an array of size 8.

* guess element = 9, count = 1, index = 0
* A[1] == guess element, count = 2, index = 0
* A[2] != guess element, count = 1, index = 0
* A[3] != guess element, count = 0 -> here as counter is 0 we change the index to the current element
  5, index = 3 and count = 1
* a[4] != guess element, count = 0 -> here again the count = 0, so we change the index to the element 
  9, index = 4, count = 1
* a[5] == guess element, count = 2, index = 4
* a[6] != guess element, count = 1, index = 4
* a[7] == guess element, count = 2, index = 4
* then check if that element is a majority element by the condition that it repeats more than half of the time
* here A[4] = 9 repeats more than half so it is a majority element

output : A[4] = 9 is the majority element 

Time Complexity = O(n)
Space Complexity = O(1)

'''

# Function to guess the maximum occurred element
def GuessMaxOccurredEle(Arr): 
    max_index = 0
    count = 1
    for index in range(len(Arr)): 
        # incrementing the count when the next element is matching our guess
        if Arr[max_index] == Arr[index]: 
            count += 1
        # decrementing the count when the next element is not same as guessed element
        else: 
            count -= 1
        # when count is 0 we are taking the current element as our guessing element
        if count == 0: 
            max_index = index 
            count = 1
    return Arr[max_index] 
  
# Function to check if the guessed element occurs more than n/2 times 
def isMostOccurredEle(Arr, guessEle): 
    count = 0
    for index in range(len(Arr)): 
        if Arr[index] == guessEle: 
            count += 1
    if count > len(Arr)/2: 
        return True
    else: 
        return False
  
# Function to print Most Occurred Element in the array
def printMostOccurredEle(Arr): 
    # edge cases
    if len(Arr) == 1:
        print("Most Occurred Element: " + str(Arr[0]))
    elif len(Arr) == 2:
        if Arr[0] == Arr[1]:
            print("Most Occurred Element: " + str(Arr[0]))
        else: 
            print(str(Arr[1]) + " must occur atleast " + str(int(len(Arr)/2) + 1) + " times.\nSo majority element not found in this Array")
    
    # for array size greater than 2
    else:
        # find the guess element that can be most occurred element in the array
        guessedMostOccurredEle = GuessMaxOccurredEle(Arr)
        # Print the guessed most occurred element in the given array if it is occurring more than size/2
        if isMostOccurredEle(Arr, guessedMostOccurredEle) == True: 
            print(guessedMostOccurredEle) 
        else: 
            print(str(guessedMostOccurredEle) + " must occur atleast " + str(int(len(Arr)/2) + 1) + " times.\nSo majority element not found in this Array")
     
  
# Input code for testing the above functions 
arr = input("Enter elements in the array: ")  # takes the whole line of n numbers
if len(arr) > 0:
    input_Array = list(map(int,arr.split(' ')))
    printMostOccurredEle(input_Array)
else:
    print("Input array is empty")

