#屏幕截屏

import os
import time
import cv2
from PIL import ImageGrab
import MySQLdb
from ygo_image_bean import YgoImageBean


# 数据库连接
def connectionMysql():
    db = MySQLdb.connect("localhost", "root", "root", "db2019", charset='utf8')
    cursor = db.cursor()
    sql = "select * from ygo_image"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            age = row[2]
            cardid = row[3]
            print ("id=%s, name=%s, age=%s, cardid=%s" % (id, name, age, cardid))
    except:
        print ("报错了")
# 屏幕截图
def screen_shoot():
    screen = ImageGrab.grab()
    path = "E:\workspace\img\screen.png"
    screen.save(path)
    print("截图完成", time.ctime())
    cv2.imread(path)
    return screen

def load_images():
    # 图片精度
    accuracy = 0.85
    # 目标文件路径
    wanted_path = "E:/workspace/target_img"
    file_list = os.listdir(wanted_path)
    for file in file_list:
        print("文件名" + file)
        return file


def loop():
    screen_shoot()

if __name__ == '__main__':
    connectionMysql()
    loop()
    load_images()
    bean = YgoImageBean(1, 2, 3, 4)
    print("id=%s, name=%s, age=%s, cardid=%s" % (bean.id, bean.type, bean.path, bean.imageName))

imagesArray = load_images()