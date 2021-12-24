




def reverse_in_place(nums):
    
    start_IDX = 0
    end_IDX = len(nums)-1

    while end_IDX > start_IDX:
        #keep swapping items
        nums[start_IDX], nums[end_IDX] = nums[end_IDX], nums[start_IDX]
        start_IDX += 1
        end_IDX -= 1
    
    return nums


our_nums = [1,2,3,4,5,6,7,8,9,10]
print(reverse_in_place(our_nums))