# 类型标注，Python 3.5

if __name__ == '__main__':
    # 一、变量
    string:str='ha'
    times: int=3
    print(string*times) # hahaha

    result:str=1+2
    print(result) #3

    # 二、参数
    def say(name:str,start:str='Hi'):
        return start+","+name
    print(say("python"))

    # 位置参数
    # 表示args所有元素都是int类型的
    def calc_summary(*args:int):
        return sum(args)
    print(calc_summary(3,1,4)) #8

    # 三、返回值
    # 单个返回值
    def say_hello(name)->str:
        return "hello,"+name
    var="python"
    print(say_hello(var))

    #多种可能的返回值
    from typing import Union,Optional
    # Union:当一个参数可能是多种类型时使用
    def resp200(meaningful)->Union[int,str]:
        return "OK" if meaningful else 200
    print(resp200(3))
    # Optional:用于表示某个类型或Null
    def get_age(name:str)->Optional[int]:
        if name=="lk":
            return 25
        return None
    print(get_age("lk"))


    # 四、关键字参数
    def calc_summary(**kwargs:int):
        return sum(kwargs.values())
    print(calc_summary(a=1,b=2))

    # 五、多个返回值
    def resp200()->(int,str):
        return 200,"ok"
    print(resp200())

    # 多种可能的返回值(3.10+)
    def resp200(meaningful)->int|str:
        return "ok" if meaningful else 200
    print(resp200(None))


class Employee:
    name:str
    age:int

    # 返回一个Employee
    def set_name(self,name)->"Employee":
        self.name=name
        return self

# 3.11以上
# from typing import Self
# class Employee2:
#     name:str
#     age:int
#
#     def set_name(self:Self,name)->Self:
#         self.name=name
#         return self