def duplicate_check(string_to_shuffle: list, start_index: int, current_main_index: int):

    '''
        Function to check if the permuation has already been identified
    '''

    for i in range(start_index, current_main_index):
        if string_to_shuffle[i] == string_to_shuffle[current_main_index]:
            return False
    return True


def backtrack(string_to_shuffle: list, start_index: int, end_index: int):

    '''
        Usage:
            string = "Cat"
            string_list = list(string)
            list_len = len(string_list)
            backtrack(string_list, 0, list_len)
        Output:
            Cat Cta aCt atC taC tCa 

    '''
    
#     base condition
    if start_index >= end_index:
        return print(''.join(string_to_shuffle), end=" ")
    else:
        for i in range(start_index,end_index):
            
            validator = True
            validator = duplicate_check(string_to_shuffle, start_index, i)
                
            if validator:
    #             shuffle
                string_to_shuffle[start_index], string_to_shuffle[i] = string_to_shuffle[i], string_to_shuffle[start_index]
    #             call the main function again
                backtrack(string_to_shuffle, start_index+1, end_index)
    #             backtrack - revert back to original
                string_to_shuffle[start_index], string_to_shuffle[i] = string_to_shuffle[i], string_to_shuffle[start_index]