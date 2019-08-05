a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
	larg=a
elif b>a and b>c:
	larg=b
else:
	larg=c
print(larg)
