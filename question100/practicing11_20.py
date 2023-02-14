print("Q16")
a=str(input("文字を入力してください:"))
b=len(a)
print(a + "の文字数:" + str(b))
print(a + "二番目の文字" + a[1])

f=open("test.txt", "w")
f.write("Hello\n")
f.write("World\n")
f.write("ShuntaUchino")
f.close()

f=open("test.txt", "r")
f_read=f.read()
print(f_read)
f.close()

ff=open("test.txt", "r")
for s_line in ff:
    print(s_line)
ff.close()

print("Q17")
a=str(input("文字を入力してください:"))
b=len(a)
print("最初:" + a[0] +"  最後:" + a[b-1])
print("最初:" + a[0] +"  最後:" + a[-1])

print("Q18")
d={}
a=str(input("文字列を入力してください："))
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)

print("Q19")
volws=["a", "i", "u", "e", "o"]
a=str(input("文字列を入力してください"))
newword=""
for i in a:
    if i in volws:
        continue
    newword+=i
print("作成した文字列" + newword)

print("Q20")
word=str(input("文字列を入力してください"))
word=word.upper()
print(word)