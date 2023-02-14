print("Q51")
t1 = (1, 2, 3)
print(t1)
l=[1, 2, 3]
t=tuple([1,2,3])
print(f'リストから作成 : {t}')

print("Q52")
t=(1,)
print("要素が1だけのタプル" + str(t))
print(type(t))

print("Q53")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ll = [tuple([i for i in l[:3]]), tuple([j for j in l[3:6]]), tuple([k for k in l[6:]])]
print(ll)
#or 
new_l = [tuple(l[i:i+3]) for i in range(0, 9, 3)]
print("答" + str(new_l))

print("Q54")
l_t = [(1,2,3),(4,5,6),(7,8,9)]
for i, j in zip(l_t, range(1,4)):
    print(f"{j}番目の値： {i[0]} {i[1]} {i[2]}")
#or 
for i , row in enumerate(l_t,start=1):
    a,b,c=row
    print(f"{i}番目の値: {a} {b} {c}")

print("Q55")
t = (1, '2', 3, '4', 5, '6', 7, '8', 9)
new_t = tuple(reversed(t))
print(new_t)

print("Q56")
t = (1, '2', 3, '4', 5)
str_t=(str(v) for v in t)
converted_int = int("".join(str_t))
print(f"変換後：{converted_int}")

print("Q57")
t = (1, [2, 3], '4', (5, 6, 7), '8', (9, 10))
count = 0
for i in t:
    if type(i) == tuple:
        count += 1 
print(f"タプル内に含まれるタプル数：{count}個")

#OR
t_in_tuple=[v for v in t if isinstance(v, tuple)]
print(f"タプル内に含まれるタプル数：{len(t_in_tuple)}")

print("Q58")
t = (1, [2, 3], '4', (5, 6, 7), None, (9, 10))
l=[]
for i in t:
    if isinstance(i, tuple):
        l.append(i)
    elif isinstance(i, list):
        l.append(tuple(i))
    else:
        l.append((i,))
print(tuple(l))


