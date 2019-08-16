# 不能重载，不能重名
# 重载就是无参数调用有参数
# py有默认值
# *list **map()
import random


def add(i, j=9):
    return i + j

print(add(1,2))

def dis0(*a):
    for i in a:
        print(i)
dis0(1,2,34,5,67,"dsa")

def dis1(**b):
    return {"name":b.get("name","xxx"),"age":b.get("age","18")}
ddd=dis1(name="zlx")
print(ddd)

def dis2(*a,**b):
    print(a)
    print(b)
    # 都可以单独传
    # 要按照顺序传
    dis2(1,23432,2,a=1,b=2)
# dis2(1,2,name=1,4) 不能交叉使用

print("++++++++++++++++++++++++++++++++++++++++")



# lambda i,j:i+j
# 只有局部变量,想用全局要global,不是全局上一层要用nolocal,看局部,不看全局

# 参数传值传lamba

def opt1(f,a,b):
    return f(a,b)
print(opt1(a=1,b=2,f=lambda g,k:g+k))

# 闭包
def opt2():
    def opt3():
        return "hello"
    return opt3
print(opt2()())

# 解构,**dict,*list

# 作业map(_+1).map,生产者消费者,调度器,list判断是否调度完

# pass 表示什么也不写,空循环

# 大括号代表set{}
aset={print("aa"),print("bb")}
print(type(aset))

# yield和return(函数)不能在一起,生成器,协程:空闲cpu时让其他人执行,cpu不闲着,异步,单线程,一个核心
# next(fun) 断点 返回值是生成器给外面的值:yield 后面的东西,p.send() 参数是给断点传的值,第一次一定要next

print("++++++++++++++++++++++++++++++++++++++++")
def myy():
    while True:
        swap=random.randint(1,10)
        print("aaa"+str(swap) )
        ss= yield swap
        print("bbb"+str(ss))
    else:pass
yyy1=myy()
getdata=next(yyy1)
print(getdata)
next(yyy1)
yyy1.send("ok")

# 调度器,询问

# for循环,in就是生成器,迭代,yield arry[i],next(),相当于while
# next(f)=f.send(null)\next没有下一个,就会报错,用try,cache
# 三条管道,0输入,1输出,3错误,三条管道并行,所以错误会

# type的type是type
# id()看内存编号,不是内存地址,整数值传递,数组是新的,内容是一样的,和java一样内存不连续
# 定长数组go,变长切片,普遍,
# 元组一般都是一样的,py不一样
# 传参数:复制一个值,给这个值贴签,写实复制

# movl $1 %eax   1就是栈,栈都是同一个地方,堆随便放
# movl %eax %ebx

# __name__对象名
print("++++++++++++++++++++++++++++++++++++++++")
if __name__=="__main__":
    print("hello")

# 属性都是public的,__是起了个名字叫私有 对象._person__id,写时复制,写一次才复制过来



class Xxx:
    def xxx(self,a,b):
        a
x=Xxx()
Xxx.a=lambda self,x,y:x+y
#属于clas的dict
Xxx.b=lambda x,y:x+y
print(x.a(1,2))
print(Xxx.a(x,1,2))
print(Xxx.b(1,2))
# vars() 和 .__dcit__一样
#next() 和__next__一样
# name
# init
# str repr
# type __class__

# @getdata set
# @Classmethod多传入一个类类型  staticmethod 静态方法 类or对象

# 反射底层是hash
# 引用计数器,del删除

# 继承就是(,)
# __mro__继承线
# __bases__父类 属性写实复制, 方法:模版调用,继承线
# 抽象 abstractmethod