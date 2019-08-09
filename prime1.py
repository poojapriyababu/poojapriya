l=int(input())
s=int(input())
for val in range(l,s+1):
	if val>1:
		for n in range(2,val):
			if(val%n)==0:
				break
		else:
			print(val)
