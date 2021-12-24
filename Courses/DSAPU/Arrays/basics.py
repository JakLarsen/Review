



#BASIC LIST COMPREHENSIONS

u = ['apple', 'orange', 'pineapple', 'raspberry', 'blueberry', 'melon']
print(u)
w = [x for x in range(1,10)]
print(w)
x  = list(range(1,10))
print(x)

y = [i for i in x if i == 8]
print(y)

z = [i for i in x if i < 6]
print(z)

a = [i**2 for i in x]
print(a)

b = [i**2 if i % 2 == 0 else i**3 for i in x]
print(b)

c = [i for i in u if "apple" in i]
print(c)

d = [i + ' is good' if 'berry' in i else i + ' is ok' for i in u]
print(d)