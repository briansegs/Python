def selection_sort(lst):
    for i_l in range(len(lst)):
        index_low = i_l
        for index_high in range(i_l+1, len(lst)):
            if lst[index_high] < lst[index_low]:
                lst[index_high], lst[index_low] = lst[index_low], lst[index_high]
    return lst

        

arr = [64, 25, 12, 22, 11] 
print(selection_sort(arr))
