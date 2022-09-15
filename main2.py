num = [0, 1, 2, 3, 4, 5, 7, 14, 35, 11, 121]
filtered_num = list(filter(lambda i: (i % 2 == 0), num))
print(filtered_num)

map_num = list(map(lambda i: (i+100), num))
print(map_num)

lambda_num = list(map(lambda i: i // 7, num))
print(lambda_num)

def mod(x):
    return x % 5
mod_num = list(map(mod, num))
print(mod_num)

new_num = [i * 0.9  for i in num]
print(new_num)

nope_num = [i for i in num if  i % 11 == 0 ]
print(nope_num)

table = [[x * y for x in range(1, 6)] for y in range(1, 6)]
print(table)

names = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
fil_names = [letter for name in names for letter in name]
print(fil_names)

print(filter_name)

num = [2, 77, 12, 3, 0, 112, 4, -987]
num1 = [i * 2 if i < 5 else i - 2 for i in num]
print(num1)

names = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
fil_names = [letter for name in names for letter in name]
print(fil_names)

def list_sort(x):
    x.sort(key=lambda i: abs(x), reverse= True)
    return x

def sum_range(start, end):

    if start > end:
        start, end = end, start
    return sum(range(start, end+1))

print(sum_range(5,3))
