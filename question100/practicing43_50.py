print("Q44")
l = [1, 2, 3, "4", 5]
if any([i for i in l if isinstance(i, str)]):
    print("文字列が入っています")
else:
    print("文字列は入っていません")

print("Q45")
l = [1, 2, 3, 4, 5]
for i in range(0, 10, 2):
    l.insert(i, 'list')
print(f'"list"を追加したリスト : {l}')

print("Q46")
l = ['Python 1', 'Java 1', 1, 'Python 2', 'Java 2', 2]
new_list = [i for i in l if (isinstance(i, int)) or (not "Python" in i)]
print(new_list)
#または
ll=['Python 1', 'Java 1', 1, 'Python 2', 'Java 2', 2]
for v in ll:
    if "Python" in str(v):
        ll.remove(v)
print(ll)

print("Q47")
l = [1, 3, 2, 3, 4, 6, 5, 8, 7]
ll = [value for index, value in enumerate(l) if not (index%3==0 and value%3==0)]
print(ll)

print("Q48")
telephone_numbers = ['080-1203-4455', '090-9372-9682', '090-3080-4982', '080-3917-5918']
ll = [i for i in telephone_numbers if i[:3] == "080"]
print(ll)

print("Q50")
l1 = [4, 6, 9, 2]; l2 = [3, 5, 7]; l3 = [1, 9, 7]
new_list = [l1, l2, l3]
sorted_new_list = sorted(new_list, key= lambda v: sum(v)/len(v), reverse=True)
print(f"平均値が高いリスト：{sorted_new_list[0]}")