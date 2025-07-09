def diff_range(n):
    if len(n) < 3:
        return "range determination not possible"
    else:
        return max(n) - min(n)

a = [5,3,8,1,0,4]
answer = diff_range(a)
print("range of the list is : ",answer)