python缓冲区:全缓冲,行缓冲,无缓冲

> * 默认文件缓冲区大小为4096
>
>   * ```python
>     f = open("a.txt", "w")
>     f.write("abc")
>     f.write("*" * 4093)
>     f.write("_")
>     ```
>
> * > 关于`__slots__`有一个常见的误解，就是将`__slots__`理解为一种封装工具，可以阻止用户为实例添加新的属性，尽管这的确是使用`__slots__`所带来的副作用，但这绝不是使用`__slots__`的原本意图，相反，人们一直以来都是`__slots__`当做一种优化工具。
>
>   `__slots__`核心作用是：可以在创建大量实例的时候更加节省内存。减少每个实例_\_dict__字典开销.
>
> * \_\_enter\_\_和\_\_exit\_\_方法实现上下文管理器,分别在with开始和结束的时候调用
>
>   * 调用\_\_enter\_\_方法有返回值,即`with open("...") as f` 中的`f`
>
>   * 而调用`__exit__`方法中
>
>     * ```python
>       def __exit__(self, exc_type, exc_val, exc_tb):  # 后三参数都是与异常相关 exc_type:异常类型, exc_val:异常值, exc_tb:异常栈
>           ...
>           return True # 这样会使得上下文捕获到的异常忽略掉
>       ```
>
> * 为什么要有`get/set`方法,而不是直接使用赋值给实例对象修改属性 `test.a = '123'`
>
>   * 无法确定用户传入的实参是否与形参类型一致,此时调用`get/set`可以在里面稍作判断
>
> * 让类支持比较操作
>
>   * ```python
>     class1 < class2 # 等效于调用 class1.__lt__(class2)
>     # 可以使用 from functools import total_ordering 装饰器就可以实现所有的比较
>     from abc import ABCMeta, abstractmethod  # 在接口中定义抽象方法
>     ```
>
> * 在使用描述符对实例属性做类型检查
>
> * 函数中的元数据
>
>   * `f.func_code` `f.func_doc` `f.func_name`... ---> `f.__name__`