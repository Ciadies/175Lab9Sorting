import random
import time

#---------------------------------------#      
# Implement Recursive selection sort here. 

# n: size of array - index is index of starting element
def swap(a, b, data):
    temp = data[a] # store the value at one position
    data[a] = data[b] #replace the now stored variable
    data[b] = temp #replace the variable with the stored variable
    
def recursive_selection_sort(data, data_len, index = 0): 
  
    # TODO-Remove pass and fill out the rest. 
    #You may use additional user_defined functions if required.
    if data_len == index: #check if the index is no longer in the list since data_len = # of elements + 1
        return data
    else:
        largest = data[index] 
        large_index = index
        for j in range(index+1, data_len): #compare against all values in the list that aren't sorted
            if data[j]>largest: #if find a new larger index, update refrences
                largest = data[j]
                large_index = j
        swap(index, large_index, data) #one all elements parsed, swap the overall largest and the element and position index
        
        recursive_selection_sort(data, data_len, index+1) #recursively call for the list with the next index     

#---------------------------------------#
#Implement the Recursive merge sort here
def merge(data_a, data_b):
    communal = [] 
    while len(data_a) != 0 and len(data_b) != 0: #combines the two lists into a sorted order until one of them is empty
        if data_a[0] > data_b[0]:
            communal.append(data_a.pop(0))
        else:
            communal.append(data_b.pop(0))
    if len(data_a) != 0 and len(data_b) == 0: #Empties the non empty, sorted list into the main list once it's counterpart is empty
        while len(data_a) != 0 :
            communal.append(data_a.pop(0))
    if len(data_b) != 0 and len(data_a) == 0:
        while len(data_b) != 0 :
            communal.append(data_b.pop(0))
    
    return communal
def recursive_merge_sort(data): 
    
    # TODO-Remove pass and fill out the rest. 
    #You may use additional user_defined functions if required.
    if len(data) == 1 or len(data) == 0: #if list is one or 0 elements already sorted
        return(data)
    elif len(data) == 2: #if list is 2 elements, check if sorted, if not, swap the two values
        if data[0] < data[1]:
            swap(0,1,data)
            return data
    else:
        middle = round((len(data)/2)) #find middle
        data_a = recursive_merge_sort(data[:middle]) #all values to left of middle
        data_b = recursive_merge_sort(data[middle:]) #all values to right of middle
        data = merge(data_a, data_b)
    return data
     
#---------------------------------------#
if  __name__== "__main__":
    # Define the list of random numbers
    random_list = [random.randint(1,1000) for i in range(500)]
    list_len = len(random_list) 
    ascending_list = sorted(random_list)
    descending_list = sorted(random_list, reverse=True)
      
    # Calculate the execution time to sort a list of random numbers #
    random_list_ = random_list.copy()  # make a copy to save the unsorted list
    start_sel = time.time()
    recursive_selection_sort(random_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(random_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of random numbers
    print('The execution time: to sort a random list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
    
    
    # Calculate the execution time to sort a list of intergers already sorted in ascending order #
    ascending_list_ = ascending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(ascending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(ascending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in ascending order 
    print('The execution time: to sort a ascending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))      
    
    
    # Calculate the execution time to sort a list of intergers already sorted in descending order #
    descending_list_ = descending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(descending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(descending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in descending order 
    print('The execution time: to sort a descending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
