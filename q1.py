def count_pairs(a,target_sum):
    count = 0
    n = len(a)

    for i in range(n):
        for j in range(i+1,n):
            if a[i] + a[j] == target_sum:
                count += 1
    
    return count

a = [2,7,4,1,3,6]
target_sum = 10
result = count_pairs(a,target_sum)
print("the follwing pair with the sum  in the given list is : ",result)