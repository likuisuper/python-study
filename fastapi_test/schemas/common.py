from enum import Enum


# 注意，由于fastapi使用Pydantic 来作为字段类型，所以要将ModelName转换为Pydantic类型，比如Enum，或BaseModel等
# 在Pydantic中，虽然str是一个字段类型，但在FastAPI中，对于路径参数和请求体参数，FastAPI需要能够验证和转换输入数据的能力
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
