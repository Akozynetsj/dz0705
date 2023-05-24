#4
def func_4(*args):
    dict1 = {}
    for name, age in args:
        dict1[name] = age
    return dict1
print(func_4(*[('Kaeya', 24), ('Diluc', 24), ('Albedo', 5000), ('Tartaglia', 20)]))