# 1.函数的 参数和 返回值，一个函数可以接收 任意多个参数 或者 一次返回多个数据
# 有关 函数的参数 和返回值


# 2.格式字符串,格式化字符串后后面()本质上是一个元组
info_tuple = ('小明', 19, 1.85)

print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple

print(info_str)
# 3.让列表不可被修改,以保护数据安全


"""
tuple(列表)=>转化为元组
list(元组)=>转化为列表
"""