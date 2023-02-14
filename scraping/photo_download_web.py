import os
from time import sleep

import pandas as pd
import requests

IMAGE_DIR = "../../../Documents/python/images/"

if os.path.isdir(IMAGE_DIR):
    print("ファイルは既にあります")
else:
    os.makedirs(IMAGE_DIR)

#csvの読み込み
df = pd.read_csv("yahoo_img.csv")

#画像の保存
for file_name, yahoo_image_url in zip(df.filename[:4], df.img_url[:4]):
    image = requests.get(yahoo_image_url)

    with open(IMAGE_DIR + file_name + ".jpg", "wb") as f:
        f.write(image.content)

sleep(1)