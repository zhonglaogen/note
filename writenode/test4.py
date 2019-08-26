# class的句子顺序执行，不用调用，def的句子调用才会执行
# _slots_ 可以加一个dict，通过dict给对象加属性，相当于get和set，dict是只读的，不能写。。.slots让dict不可写
# type可以造类（object）
# exception
# model
# 反射
import sys


class A:
    pass
class B:
    pass
a=globals()["A"]
print(globals()["A"])
setattr(a,"aaa",1)
setattr(a,"aA1",lambda a:print("print",a))
print(a)
a.aA1(1)
# 继承
print(dir(a))
print(B.__dict__)
# print(B.__dict__.__dict__)
# print(B.__dict__.__dict__.__dict__)
# setattr(B,A.__dir__,A.__dict__)
b=globals()["B"]
# b.aA1(1)
# 拿到所有的moudle
print(sys.modules)
# 拿到某个确定的model
print(sys.modules[__name__])
# type
# 类（）调用init，对象（）调用__call__,方法也是class，内部实现__call__方法，调用方法就是调用call
# type创建对象
# Test=type("Test", (继承类，), {'myset': mysetfun,'myget':mygetfun})
# 继承type可以造类，metaclass
# 声明了metaclass的会先调用metaclass的new和init，
# 创建对象默认调用的是metaclass的call方法，然后在call方法里面调用实际的new和init
# 字符串运行脚本，程序