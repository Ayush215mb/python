list1="11,2,3,44,4,55,67,98"
print("original list:",list1)
n=len(list1)
for i in range(n):
    for j in range(0,n-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print("list after sorting:",list1)
