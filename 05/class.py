# 面向对象

# 类
class Document():
    def __init__(self, title, author, context):
        print("调用构造函数")
        self.title = title
        self.author = author
        self.__context = context  # 私有属性

    def get_context_length(self):
        return len(self.__context)

    def intercept_context(self, length):
        self.__context = self.__context[:length]


class Document2():
    # 常量
    WELCOME_STR = "欢迎，本书的内容为:{}"

    def __init__(self, title, author, context):
        print("调用初始函数")
        self.title = title
        self.author = author
        self.__context = context  # 私有属性

    # 类函数
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context="nothing")

    # 成员函数
    def get_context_length(self):
        return len(self.__context)

    # 静态函数
    @staticmethod
    def get_welcom(context):
        return Document2.WELCOME_STR.format(context)


# 类的继承
class Entity():
    def __init__(self, object_type):
        print("父类构造函数")
        self.object_type = object_type

    # 强制子类重写父类函数以免这里抛出异常
    def get_context_length(self):
        raise Exception("没有定义get_context_length")

    def print_title(self):
        print(self.title)


class Document3(Entity):
    def __init__(self, title, author, context):
        # 子类构造函数执行时机在父类构造函数之前
        print("子类构造函数")
        Entity.__init__(self, "document")
        self.title = title
        self.author = author
        self.__context = context

    def get_context_length(self):
        return len(self.__context)


# 抽象函数和抽象类
from abc import ABCMeta, abstractmethod


class Entity2(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self):
        pass


class Document4(Entity2):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title


if __name__ == '__main__':
    harry_potter_book = Document("hp", "j.k", "sfsfsfsfsdfsdfwewrw")
    print(harry_potter_book.title)
    print(harry_potter_book.author)
    print(harry_potter_book.get_context_length())
    harry_potter_book.intercept_context(10)
    print(harry_potter_book.get_context_length())
    # 报错，私有属性不允许访问
    # print(harry_potter_book.__context)

    empty_book = Document2.create_empty_book("aaaa", "bbbb")
    print(empty_book.get_context_length())
    print(empty_book.get_welcom("sfsfsfsf"))

    # 类继承
    hp_book = Document3("a", "aa", "aaa")
    print(hp_book.object_type)
    print(hp_book.get_context_length())
    hp_book.print_title()

    # 抽象类
    # 不能实例化抽象类，否则报错
    # entity=Entity2()
    document = Document4()
    document.set_title("hp")
    print(document.get_title())
