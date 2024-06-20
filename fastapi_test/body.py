from fastapi import FastAPI

from fastapi_test.schemas import Item

app = FastAPI()


# 使用pydantic模型声明的请求体
@app.post("/items")
async def create_item(item: Item):
    print(item.name)
    print(item.json)

    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict["price_with_tax"] = price_with_tax

    return item_dict


# 请求体+路径参数,fastapi能识别与路径参数匹配的函数参数，还能识别从请求体中获取的类型为pydantic模型的函数参数
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    # 这里使用了解包，**用于字典
    print(item.dict())
    return {"item_id": item_id, **item.dict()}


# 请求体+路径参数+查询参数
@app.put("/items2/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
