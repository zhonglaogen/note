mylist=["9","8","dasdadq","9","5","4"]
print(mylist)
mylist[2]="aaaa"
mylist.append("xxx")

print("*****************************************************")
mytuple=(1,"小明","男",25)
mytuple2=(2,"小华","男",21)
tup=(1,)
print(mytuple)
(id,name,sex,age)=mytuple
print(str(id)+" "+name+" "+sex+" "+str(age))
print(mytuple[2])
print(mytuple[0:])
print(mytuple[1:2])
print(mytuple*2)
print(mytuple+mytuple2)
# mytuple[0:2]=[]  #tuple不能修改
#()to string
print(mytuple.__str__()+"xxx")
print(mytuple[1:3])


