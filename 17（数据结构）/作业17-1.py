

class Set1(object):
    def __init__(self,*args):
        self.size=1007
        self.data=[]
        for i in args:
            self.data.append(i)

    def remove(self,x):
        self.data.remove(x)
    def add(self,i):
        self.data.append(i)
    def has(self,x):
        a=False
        for i in self.data:
            if i == x:
                a=True
        return a
    def __repr__(self):
        return str(self.data)
    # def __eq__(self):
    #     return str(self.data)
# def test():
#     a = Set1(1, 2, 2, 3, 4, 4)
#     b = Set1(1, 2, 2, 3, 4)
#     assert (a != b)
#     print(a)
#     print(a.data)
#     print(a.has(1))
# test()

#
# 作业二：
# 在作业一的基础上，在Set类里增加 __repr__  和 __eq__ 两个成员函数。
# 并通过附带 testSet() 函数的测试。
# 形式如下：
# class Set(object)：
#     # ...
#     def __init__(self, *args)
#         self.data = []
#
#     def __repr__(self):
#         pass
#
#     def __eq__(self, other):
#         pass
#
#     def remove(self, x):
#         pass
#     def add(self, x):
#         pass
#     def has(self, x):
#         pass
#
# def testSet():
#     a = Set(1, 2, 2, 3, 4, 4)
#     b = Set(1, 2, 2, 3, 4)
#     c = Set(1, 3, 4, 2)
#     d = Set(2, 3)
#     assert (str(a) == '{1, 2, 3, 4}')
#     print(a, b, c, d)
#     assert (a == b)
#     assert (a == c)
#     assert (a != d)
#     assert (a.has(1) == True)
#     a.remove(1)
#     assert (a.has(1) == False)
#     a.add(1)
#     assert (a.has(1) == True)
#
#
# 作业三：
# 参考第17课板书 hash_table 的代码，写一个类 Set，实现时间复杂度为O(1) 的 add,remove 函数 。
# 形式如下：
# class Set(object):
#     # ...
#     def add(self, x):
#         pass
#
#     def remove(self, x):
#         pass
class Set(object):
    def __init__(self):
        self.table_size = 7
        self.table = [0] * self.table_size

    def _insert_at_index(self, index,value):
        v = self.table[index]
        data = [value]
        if isinstance(v, int):
            self.table[index] = data
        else:
            self.table[index].append(data)
        return(self.table[index])

    def _remove_at_index(self, index,value):
            v = self.table[index]
            data = value
            if isinstance(v, int):
                self.table.remove(data)
            else:
                return None

    def add(self,value):
        index = self._index(value)
        self._insert_at_index(index,value)


    def remove(self,value):
        index = self._index(value)
        self._remove_at_index(index,value)

    def get(self, index, default_value=None):
        v = self.table[index]
        if isinstance(v, list):
            for kv in v:
                if kv[0] == index:
                    return kv[1]
        return default_value

    def _index(self, value):
        return self._hash(value) % self.table_size

    def _hash(self, s):
        n = 1
        f = 1
        for i in s:
            n += ord(i) * f
            f *= 10
        return n
def test():
    a = Set()
    print(a.add('adfa'))
    print(a.table)

test()