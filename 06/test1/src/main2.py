
# 虽然utils_with_main中有main函数，但通过import时，__name__就会被赋值为该模块的名字，自然就不等于main了，所以只会输出get_sum:3
from utils_with_main import get_sum

print('get_sum: ', get_sum(1, 2))