n=int(input("Enter Number of Elements : "))
l=[]
d={}
print("Enter Elements  : ")
for i in range(n):
	x=(int(input()))
	l.append(x)
	if x not in d.keys():
		d[x]=1
	else:
		d[x]+=1
print("Mean : ",sum(l)/n)
mxx=mkx=0
for k,v in d.items():
	if v>mxx:
		mxx=v
		mkx=k
l.sort()
print("Sorted  : ",l)
if n%2==0:
	print("Median : ",(l[n//2-1]+l[n//2])/2)
else:
	print("Median : ",l[n//2])
print("Mode : ",end="")
for k,v in d.items():
	if v==mxx:
		print(k,end=", ")
print()
