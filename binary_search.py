"""
Binary Serach:-- it will only work on sorted arrays



"""

def binary_search(arr, target):
    
    L=0
    R=len(arr)-1
    
    while R >= L:
        
        M = L + ((R-L)//2)
        
        if arr[M] == target:
            return True
        elif arr[M] < target:    
            L = M+1
        else:
            R = M-1
    return False
    

print(binary_search([-3,-2,-1,0,1,2,3], 0))
