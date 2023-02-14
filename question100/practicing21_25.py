print("Q21")
word=str(input("文字列を入力してください"))
a=""
if word[0]==word[0].upper():
    print(word*2)
else:
    for i in word:
        if i == word[0]:
            i=word[0].upper()
            a+=i
        else:
            a+=i
    print(a)

print("Q22")
word_1=str(input("1つ目の文字列を入力してください"))
word_2=str(input("2つ目の文字列を入力してください"))
j=0; a=""
for i in word_1:
    if i == word_2[j]:
        a+=i
    else:
        continue
    j+=1
print(a)
j=0; b=""
for i in word_1:
    if word_1[j]==word_2[j]:
        b+=word_1[j]
    else:
        continue
    j+=1
print(b)

print("Q23")
sentence_1=str(input("1つ目の英文を入力してください"))
sentence_2=str(input("2つ目の英文を入力してください"))
sen1=sentence_1.split()
sen2=sentence_2.split()
r=[]

for i in sen1:
    if i in sen2 and not i in r:
        r.append(i)
print("重複する単語："+ str(r))

print("Q24")
word=str(input("英単語を入力してください"))
count=0
#for _ in word:
 #   count+=1
count=len(word)

index=count // 2

if count % 2 == 0:
    word=word[0:index] + "@" + word[index:]
else:
    word=word[:index] + "@" + word[index+1:]
print("変換した単語:" + word)

print("Q25")
word_1=str(input("1つ目の英単語を入力してください"))
word_2=str(input("2つ目の英単語を入力してください"))
word_3=str(input("3つ目の英単語を入力してください"))

r=[word_1, word_2, word_3]
r.sort()
print("並び替え：\n"+ str(r))