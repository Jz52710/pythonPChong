import re

# a = re.search(r'\w+','abfc123j7')
# print(a.group())

# a = re.match(r"\d+","123abf")
# print(a.group())
#
# a = re.split("[.;]",'abc.def;ppp')
# print(a)

obj = re.finditer("哪吒","哪吒之魔童降世，哪吒")
print(obj) # ['哪吒', '哪吒']

