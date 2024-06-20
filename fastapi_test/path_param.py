# 一、导入fastapi
from fastapi import FastAPI

from fastapi_test.schemas import ModelName

# 二、创建FastAPI实例
app = FastAPI()


# 三、创建一个路径操作
@app.get("/")
async def root():
    return {"message": "hello word"}


# 路径参数
@app.get("/item/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# 声明路径参数的类型，类型声明将为函数提供错误检查、代码补全等编辑器支持
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item": item_id}


# 路径操作是按顺序依次运行的，所以/users/me一定要在/users/{user_id}前面，否则/users/{user_id}将匹配/users/me
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "deep learning ftw"}
    if model_name.value == 'lenet':
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "have some residuals"}


if __name__ == '__main__':
    # 类似于tomcat服务器
    import uvicorn

    uvicorn.run(app)
