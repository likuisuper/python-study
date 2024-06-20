from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name", "Baz"}]


# 参数是可选的，如果不设置，那么就是声明的默认值
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]


# 可选参数,fastapi可以识别出item_id是路径参数，q是查询参数，因为默认值为=None,|这种写法要3.11以上，否则要使用Union[str,None]=None
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# 查询参数类型转换,short无论传的什么，都会被转换成bool
@app.get("/items2/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"desc": "no"})
    return item


from typing import Union


# 多个路径和查询参数,声明查询参数的顺序并不重要
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(item_id: str, user_id: int, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# 必选查询参数。如果只想把参数设为可选，但又不想指定参数的值，那么把默认值设为None
# 如果要把查询参数设置为必选，就不要声明默认值
@app.get("/items3/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

# item_id,needy:必须的str类型参数
# skip:默认值为0的int类型参数，可选
# limit：可选的int类型参数，默认值为None
# 总结：包含默认值的参数是可选的、默认值为None的参数也是可选的
@app.get("/item4/{item_id}")
async def read_user_item(
        item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
