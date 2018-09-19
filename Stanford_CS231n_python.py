import math


arr = [1,2,4,2,5,6,1,4,9]
print sorted(arr)   # get: [1, 1, 2, 2, 4, 4, 5, 6, 9]

print '%d,%.2f' % (arr[0],arr[1]) #   1,2.00

# python has bool compute but use 'and' 'or' not && ||
t = True
f = False
print type(t) # Prints "<type 'bool'>"
print t and f # Logical AND; prints "False"
print t or f  # Logical OR; prints "True"
print not t   # Logical NOT; prints "False"
print t != f  # Logical XOR; prints "True"  

# Python is powerful in string process with many methods
# we can use ' or " to create string

s = "hello"
print s.capitalize()  # Capitalize a string; prints "Hello"
print s.upper()       # Convert a string to uppercase; prints "HELLO"
print s.rjust(7)      # Right-justify a string, padding with spaces; prints "  hello", two spaces + hello
print s.center(7)     # Center a string, padding with spaces; prints " hello "
print s.replace('l', '(ell)')  # Replace all instances of one substring with another;
                               # prints "he(ell)(ell)o"
print '  world '.strip()  # Strip leading and trailing whitespace; prints "world"

# Python has 4 Containers that's 列表（lists）、字典（dictionaries）、集合（sets）和元组（tuples）
# 列表就是Python中的数组，但是列表长度可变，且能包含不同类型元素。
#在编程的时候，我们常常想要将一种数据类型转换为另一种。下面是一个简单例子，将列表中的每个元素变成它的平方。
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print squares   # Prints [0, 1, 4, 9, 16]

#字典用来储存（键, 值）对，这和Java中的Map差不多。你可以这样使用它
d = {key1 : value1, key2 : value2 } #一个键对应一个值

