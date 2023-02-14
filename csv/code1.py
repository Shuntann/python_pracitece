import csv
import pandas as pd
import sys

if __name__ == "__main__":

    file_name = sys.argv[1] #コマンドラインからcsvfilenameを取る
    total = 0

    with open("gameLog.csv", "r") as f:#ファイルオープン
        reader = csv.reader(f)#ゲームログファイル読み込み
        i = 0

        for line in reader:#一行目からループ
            if i <= 0:#ヘッダ巻き込み防止
                i+=1
                continue

            else:#数値読み取り作業
                print(i)
                score = int(line[2])
                total +=score
                i+=1

    
    score_ave = total/(i-1)#整数の平均値算出
    print(int(score_ave))


name_list#csvファイルから取る
dict = {"taro":200, "yasu":300, "kei":500}#得点表
dict2= {"taro":4,"yasu":2,"kei":5}#回数表
dict3={}#名前と平均値

j=0 #プレイ階数（平均値算出用）
for line in csv_list:
    if i <=0:
        i+=1
        continue
    else:
        if name1 in name_list:
        dict[name1]+= new_score#スコア合計
        dict2[name1]+=1#プレイ回数

        else:
            dict[name1]=new_score#初得点
            dict2[name1]=1#1プレイ目
            name_list.append(name1)
            

ave_list=[]

for name in name_list:
    ave = dict[name]/dict2[name]#一人分の平均値算出
    ave_list.append(ave)#各平均値をリストに格納

for name, ave in zip(name_list, ave_list):
    dict3[name]=ave #名前と平均値を一元管理できるように辞書に格納

rank_name=[]
rank_score=[]

q = len(dict3)

for name in name_list:
    score = dict3[name] #各プレイヤーの得点

    for score2, t in enumerate(rank_score, start=0):
        if score > score2:
            


    



            

