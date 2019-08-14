def findSum(n,k):
	ans=0
	for i in range(1,n+1):
		ans+=(i%k)
	return ans
n=int(input())
k=int(input())
print(findSum(n,k))
