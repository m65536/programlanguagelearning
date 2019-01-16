# -*- coding: utf-8 -*-

# list
list = ['Michael', 'Bob', 'Tracy']
print list[0]

# 倒序访问
print list[-1]

for item in list:
    print item

# 元祖
# tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。

t = ('Adam', 'Lisa', 'Bart')
print t[1]
for item in t:
    print item


# dic
"""
dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。

不过dict的查找速度快不是没有代价的，dict的缺点是占用内存大，还会浪费很多内容，list正好相反，占用内存小，但是查找速度慢。

由于dict是按 key 查找，所以，在一个dict中，key不能重复。

dict的第二个特点就是存储的key-value序对是没有顺序的！这和list不一样：
"""

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print d['Adam']

# set
"""
dict的作用是建立一组 key 和一组 value 的映射关系，dict的key是不能重复的。

有的时候，我们只想要 dict 的 key，不关心 key 对应的 value，目的就是保证这个集合的元素不会重复，这时，set就派上用场了。
"""
s = set(['A', 'B', 'C'])
print s
