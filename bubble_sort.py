

num_list = [20000,4000,600,80,10]


for num_rev_ind in range(len(num_list) - 1, 0, -1):

    for idx in range(num_rev_ind):

        if num_list[idx] > num_list[idx + 1]:
            hold = num_list[idx] 
            num_list[idx] = num_list[idx + 1]
            num_list[idx + 1] = hold
            
        
print(num_list)
