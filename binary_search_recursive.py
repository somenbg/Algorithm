def binary_search_recursive(list_to_search: list, start_index: int, end_index: int, element_to_search: int):

    '''
        Usage:
            list = [1,2,3,4,5,6]
            binary_search_recursive(list, 0, len(list1)-1, 1)
        Output:
            "Element '1' is at index '0'"
    '''
    
    if start_index <= end_index:
        
        mid_index = (start_index+end_index)//2

        if list_to_search[mid_index] < element_to_search:
            return binary_search_recursive(list_to_search, mid_index+1, end_index, element_to_search)
        
        elif list_to_search[mid_index] > element_to_search:
            return binary_search_recursive(list_to_search, start_index, mid_index-1, element_to_search)
        
        else:
            return "Element '{}' is at index '{}'".format(element_to_search, mid_index)
    
    else:
        return "Element {} is not in the list".format(element_to_search)