def reverse_an_arr(arr,n,i):
    if ((n/2)+1)<=i:
        return arr
    arr[n],arr[i]=arr[i],arr[n]
    reverse_an_arr(arr,n-1,i+1)

arr=[1,2,3,4,5,6,7]
reverse_an_arr(arr,6,0)
print(arr)