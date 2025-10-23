def my_function(*args, **kwargs):
    kwarg_values = set(kwargs.values())
    count = 0
    for arg in args:
        if arg in kwarg_values:
            count += 1
    return count

result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)