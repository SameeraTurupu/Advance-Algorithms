'''
Given n elements in an array find the minimum and maximum element simultaneously with floor(1.5n)-2 comparisons

Algorithm:

* Case 1: Size of the array is Odd
        initialize the first element as both min and max elements
* Case 2: Size of the array is Even
        compare first two elements and assign them to min and max variable accordingly
* take the remaning elements in pairs and compare them 
* the minimum and maximum values in the pair are again compared with min and max variables 
and updated accordingly.

For Example:
        
     Odd -   A = [2, 100, 50, 7, 10]
      
    1. min = 2, max = 2
    2. first pair (100, 50) - comparing them min' = 50, max' = 100 
       then min < min' so no change, max' > max so max = max' so min = 2, max = 100
    3. second pair (7, 10) - comparing them min' = 7, max' = 10
       then min < min' so no change, max > max' so no change
    
    output: min = 2, max = 100

    Time complexity for odd sized array = 3(n)/2
                      comparision between pairs + comparing min with min' + comparing max with max' = 3 each time
                      (n)/2 as taking 2 elements each time excluding first element

     Even - A = [2, 100, 50, 7, 10, 500]

     1. A[0] < A[1] so min = 2, max = 100
     2. first pair (50, 7) - comparing them min' = 7, max' = 50
        then min < min' so no change, max > max' so no change - min = 2, max = 100
     3. second pair (10, 500) - comparing them min' = 10, max' = 500
        then min < min' so no change, max' > max so max = max' - min = 2, max = 500
    
    output: min = 2, max = 500

    Time Complexity for even sized array = 3n/2 - 2
                         comparision between the first two elements = 1
                         comparision between pairs + comparing min with min' + comparing max with max' = 3 each time
                         (n)/2 as taking 2 elements each time excluding first two elements

'''
def findMinMax(arr): 
      
    size = len(arr) 
    if (size == 1):
        return (arr[0], arr[0])
    elif (size == 2):
        return (arr[0] if (arr[0]>arr[1]) else arr[1], arr[0] if (arr[0]< arr[1]) else arr[1]) 

    else:
        # initialize the first two elements as minimum and maximum if they are even number of elements in this array
        if(size % 2 == 0): 
            maxEle = max(arr[0], arr[1]) 
            minEle = min(arr[0], arr[1]) 
            # setting the starting index for loop  
            index = 2
        # initialize the first element as minimum and maximum if they are odd number of elements in this array
        else: 
            maxEle = minEle = arr[0] 
            # setting the starting index for loop   
            index = 1
        #taking remaining elements in pair and comparing them with the minEle and maxEle and updating them accordingly  
        for index in range(index, size - 1, 2):
            if arr[index] < arr[index + 1]: 
                maxEle = max(maxEle, arr[index + 1]) 
                minEle = min(minEle, arr[index]) 
            else: 
                maxEle = max(maxEle, arr[index]) 
                minEle = min(minEle, arr[index + 1]) 
        return (maxEle, minEle) 
      

# Input code for testing the above functions 
arr = input("Enter elements in the array: ")  # takes the whole line of n numbers
if len(arr) > 0:
    input_Array = list(map(int,arr.split(' ')))
    maxEle, minEle = findMinMax(input_Array)
    print ("minimum and maximum elements of the given array are: ", minEle, maxEle)
else:
    print("Input array is empty")

    



