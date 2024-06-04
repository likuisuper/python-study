# 字典和集合

products = [(1, 100), (2, 400), (3, 50), (4, 400)]


# 根据商品id求价格，用列表
def find_product_price(products, product_id):
    for id, price in products:
        if id == product_id:
            return price;
    return None


# 更改需求，找出有多少种不同的价格
def find_unique_price(products):
    unique_price_list = []
    for _, price in products:
        if price not in unique_price_list:
            unique_price_list.append(price)
    return len(unique_price_list)


# 字典版
def find_unique_price_set(products):
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)


if __name__ == '__main__':
    # 初始化字典和集合
    d1 = {"name": "jason", "age": 20, "gender": "male"}
    d2 = dict({"name": "jason", "age": 20, "gender": "male"})
    d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
    d4 = dict(name='jason', age=20, gender='male')
    print(d1 == d2 == d3 == d4)

    s1 = {1, 2, 3}
    s2 = set([1, 2, 3])
    print(s1 == s2)

    # 混合类型
    s = {1, "hello", 5.0}
    print(s)

    # 元素访问
    d = {"name": "lk", "age": 20}
    print(d["name"])
    print(d.get("age"))
    print(d.get("locate", "null"))

    # 判断元素是否在字典/集合内
    s = {1, 2, 3}
    print(1 in s)
    print(10 in s)
    print("name" in d)
    print("location" in d)

    # 增删改查函数
    d["gender"] = "male"  # 增加元素
    d["dob"] = "2029-12-12"
    print(d)
    d["dob"] = "2021-12-10"  # 更新键值
    print(d)
    d.pop("dob")  # 删除键值
    print(d)

    s.add(4)  # 增加元素
    print(s)
    s.remove(4)  # 删除元素
    print(s)

    # 字典排序
    d = {'b': 1, 'a': 2, 'c': 10}
    print(d.items())

    # sorted函数的参数有两个，第一个参数是一个*，表示类型是集合，第二个参数是两个*，表示类型是dict
    # key定义了排序的关键字,x[0]表示使用字典的键排序，x[1]表示使用字典的value排序
    # 根据字典键的升序排序
    d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])
    print(d_sorted_by_key)
    # 根据字典值的升序排序
    d_sorted_by_value = sorted(d.items(), key=lambda x: x[1])

    # 对集合排序。sort只能用于列表排序，并且没有返回值，但是sorted可以对列表、元组、字典排序，并且有返回值，不会影响原来排序的对象
    s = [3, 4, 2, 1]
    s_sorted = sorted(s)
    print(s_sorted)

    # 根据商品id找商品价格
    print("id为2的商品价格为{}".format(find_product_price(products, 2)))

    # 用字典来存储
    products_set = {
        1: 100,
        2: 400,
        3: 50,
        4: 400
    }
    print("id为3的商品价格为{}".format(products_set[3]))

    # 看商品有多少种不同的价格
    # 列表版，O(N^2)
    print("不同价格的数目为{}".format(find_unique_price(products)))
    # 字典版，0(N)
    print("不同价格的数目为{}".format(find_unique_price_set(products)))
