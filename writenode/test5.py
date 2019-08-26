# inspect.isclass() 判断是否是类
# @yyy
# xxx
# 装饰器
# yyy(xxx)()
# 触发器,其实就是=的重载

class decri:
    def __init__(self):
        print("decri init")
    def __set__(self, instance, value):
        print("set")
        print(instance)
    def __get__(self, instance, owner):
        print("get")
    def __del__(self):
        print("del")
class mytest:
    def xxx(self):
        print("xxx")
    dec=decri()
my=mytest()
my.dec
my.dec=9

# type可以创建对象：type（类，父类，方法）
# type（对象）得到类
# 类调用new，init，添加这个类作用域
# 类（）调用call，调用类的new，init

# moudle就是x.py
# import就是创建module对象

# 自己，父类，instance

# r字符串不转义，b二进制，u是Unicode

# slot是通过对象给类加属性