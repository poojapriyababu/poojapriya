import statistics
m=int(input())
arr=[]
for i in range(m):
	x=int(input())
	arr.append(x)
w=arr.sort()
median=statistics.median(arr)
print(median)
