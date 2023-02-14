print("Q26")
l = [1, 2, 3, 4, 5]
total=0
for i in l:
    total+=i
print(str(total))

print("Q27")
l = [1, 2, 3, 4, 5]
print("合計:"+ str(sum(l)))

print("Q28")
l = [1, 5, 3, 2, 4]
max=0; j=0
for i in l:
    if i > max:
        max=i
print(str(max))

print("Q30")
l = [1, 2, 2, 3, 3, 4, 5]
ll=list(set(l))
print(ll)

print("Q31")
l = ['PHP', 'Ruby', 'Python', 'JavaScript']
a=l[0]
for i in l:  
    if len(i) < len(a):
        a=i
print(a)

print("Q32")
l = ['Python', 'Ruby', 'PHP', 'JavaScript']
ll=sorted(l,key=len)
print("短い順番に並び替えられたリスト"+ str(ll))

print("Q33")
l1 = ['Python', 'Ruby', 'PHP', 'JavaScript', "Java"] 
l2 = ['Java', 'Ruby', 'Golang', 'Python', 'TypeScript', "Java"]
ll=[]; lr=[]
for i in l1:
    if i in l2:
        ll.append(i)
print("共通の値："+ str(ll))

for word1 in l1:
    for word2 in l2:
        if word1 == word2 and word1 not in lr:
            lr.append(word1)
print("共通の値："+ str(lr))

print("Q34")
l = ['1', 2, '3', 4, '5', 6, '7', 8, '9', 10]
print(f'偶数のインデックス番号 : {l[::2]}')

print("Q35")
l = ['1', 2, '3', 4.0, '5', 6, '7', 8.0, '9', 10]
ll=[]
for i in l:
    if isinstance(i, int):
        ll.append(i)
print(f"整数型に絞り込んだリスト：{ll}")

print("Q36")
l = [[5*i + j for j in range(1, 6)] for i in range(2)]
l1=list(range(1,5))#これでリストの作成
print(f'作成したリスト : {l}')

print("Q37")
l = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
newlist1=[]

#for i in l:
 #   newlist1+=i
newlist1=[i for row in l for i in row]
print(f"新しいリスト：{newlist1}")

print("Q38")
list_number1=input("最初の数字")
list_number2=input("真ん中の数字")
list_number3=input("最後の数字")
list=[list_number1, list_number2, list_number3]
print(list)

l = []
if l:
    print(f'入力されたリスト : {l}')
else:
    print(f'入力されたリストは空でした。')

print("Q39")
l1 = [1 ,2 ,3, 4, 5] 
l2 = [10, 9, 8, 7, 6]
new_list=[i*j for i, j in zip(l1, l2)]
#j=0
#for i in l1:
#    new_list.append(i*l2[j])
#    j+=1
print(new_list)

print("Q40")
l = [1, '22', 3, '444', 0.0, '5']
new_l = [v for v in l if isinstance(v, int)]

print("Q41")
l = [0, '1', 3, 2, '4', 5, '7']
new_l = [object for i, object in enumerate(l) if i == int(object)]
print(f'インデックスと値が一致 : {new_l}')

print("Q42")
l=[1,2,2,4]
j=1
for i in l:
    if i in l[j:len(l)]:
        print("重複している値がある" )
        break   
    elif j == len(l):
        print("重複している値なし")    
    j+=1

print("Q43")
l = [1, 'aaa', 2, 'bbb', 'ccc', 3, 'ddd', 4]
#int_list=sorted([i for i in l if isinstance(i, int)])
int_list=sorted([i for i in l if isinstance(i, int)])
str_list=([w for w in l if isinstance(w, str)])
print(f"ソートしたリスト {int_list + str_list}")

