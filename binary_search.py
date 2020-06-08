def binary_search(list_to_search: list, element_to_search: int):

    '''
        Usage:
            list = [1,2,3,4,5,6]
            binary_search(list, 4)
        Output:
            "The element's index is: 3"
    '''
    
    first_index = 0
    last_index = len(list_to_search) - 1
    
    while first_index <= last_index:
        
        mid_index = (first_index+last_index)//2
        
    
        if list_to_search[mid_index] == element_to_search:
            return "The element's index is: {}".format(mid_index)

        if element_to_search > list_to_search[mid_index]:
            first_index = mid_index + 1
        else:
            last_index = mid_index - 1
            
    if first_index > last_index:
        return "Searched element {} is not in list".format(element_to_search)