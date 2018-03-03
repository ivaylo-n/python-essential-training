
x = (1, 'two', 3.0, [4, 'four'], 5)
y = [1, 'two', 3.0, [4, 'four'], 5]
print('x is {}'.format(x))
print(type(x[1]))
print(id(x))
print(id(y))

if x[0] is y[0]:
    print('yep')
else:
    print('nope')

if isinstance(y, tuple):
    print('tuple')
elif isinstance(y, list):
    print('list')
else:
    print('nope')
