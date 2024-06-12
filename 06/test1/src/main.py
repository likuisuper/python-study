
# import在导包的时候会自动把所有暴露在外面的代码全都执行一遍，所以get_sum中的打印内容都会执行
from utils import get_sum

print('get_sum: ', get_sum(1, 2))