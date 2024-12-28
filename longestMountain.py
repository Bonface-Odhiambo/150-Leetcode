def longestMountain(arr):
    if len(arr) <3: #Handling the base case where there cannot be a mountain peak
        return 0
    

    ret = 0

    for i in range(1, len(arr)- 1):
        #check if current position is a peak
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            #Initialize left and right pointers
            l = i
            r = i


            #Expand left while ascending
            while 1>0 and arr[l-1]< arr[l]:
                l -=1

            #Expand right while descending
            while r < len(arr)-1 and arr[r] > arr[r+1]:
                r +=1


            #Update maximum length
            ret = max(ret, r-l+1)


    return ret


