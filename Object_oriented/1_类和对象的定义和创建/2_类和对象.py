"""
python中一切皆为对象
Python 中，一切皆对象。每个对象由：标识{内存地址}（identity）、类型（type）、value（值）
组成。

变量位于：栈内存。
对象位于：堆内存。

类和对象的概念：
类就是一个模板，模板里可以包含多个函数，函数里实现一些功能；
对象则是根据模板创建的实例，通过实例对象可以执行类中的函数。
对象和定义类：
使用class语句来创建一个新类，class 之后为类的名称并以冒号结尾；
实例化其他编程语言中一般用关键字new ，但是在python中并没有这个关键字，类的实例化类似函数调用方法
实例方法和属性：
在类的内部，使用def关键字可以定义一个实例方法，
定义在类里面， 方法外面的属性称为类属性，
定义在方法里面的使用self引用的属性称为实例属性
"""
a = 3
print(id(3))
# 1616609456
print(type(3))
# <class 'int'>
# a的id = 3的id
