print("Q1")
print("7+3="+ str(7+3))
print("7-3=" + str(7-3))
print("7*3=" + str(7*3))
print("7/3=" + str(int(7/3)) + "余り" + str(7%3))
print("7/3="+ str(float(7/3)))

print("Q2")
input1=str(input("好きな文字を入力してください > "))
print("入力された文字:" + input1)

print("Q3")
input2=int(input("好きな整数を入力してください > "))
print(str(input2) + "の二乗値" + str(input2**2))

print("Q4")
for i in range(1,31):
    print(i)
xx= range(5)
print(xx[3])

print("Q5")
a=1 ; b=31
while a<b:
    print(a)
    a+=1

print("Q6")
for i in range(3,31,3):
    print(i)

print("Q7")
for i in range(1,31):
    if i%15==0:
        print("fizzbuzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizz")
    else:
        print(i)

print("Q8")
l = []
for i in range(1, 31):
    if i % 3 == 0:
        l.append(i)
print("作成したリスト : " + str(l))

print("Q9")
d = {}
for i in range(1, 31):
    if i % 3 == 0:
        index=f"{i//3}番目"
        d[index]=i
print("作成したリスト : " + str(d))

print("Q10")
l = []
for i in range(1, 31):
    if i % 3 == 0 and '3' in str(i):
        l.append(i)
print(f'作成したリスト : {l}')
