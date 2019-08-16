print(["++".join(str(j)+"*"+str(i)+"="+str(i*j) for j in range(1,i+1)) for i in range(1,10)])
[print(''.join([str(j)+"*"+str(i)+"="+str(i*j)+"\t" for j in range(1,i+1)])) for i in range(1,10)]
[print("a"),print("d"),print("d"),print("d"),print("d"),print("d")]
print('  '.join(["aaaaaaaaaaa","das","fsaf","sdaf","adga","g"]))

[print('  '.join([str(j)+"*"+str(i)+"="+str(j*i) for j in range(1,i+1)]))for i in range(1,10)]
len=3
[print(" "*(len-i)+"*"*i+"*"+"*"*i)for i in range(0,len)]
[print(" "*(len-i)+"*"*i+"*"+"*"*i)for i in range(len-2,-1,-1)]

print()
i=2
mylist=[1,1]
while i<15:
     mylist.append(mylist[i-1]+mylist[i-2])
     i=i+1
else:
    print(mylist)
print(mylist)
print(mylist[-3:-2])

print([i for i in range(0,10)])
[print(i) for i in range(0,10)]
