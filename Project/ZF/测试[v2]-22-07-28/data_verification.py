# 添加模块
# import sys
# sys.path.append('/Users/zhouxinyu/侧边栏文件夹/Code/VSCode/Jupyter/Project/ZF/测试[v2]-22-07-28')
# from data_verification import imgs as zf_test_imgs
# from data_verification import imgs_line_pollution, dir_line_damage, imgs_barrel_pollution, imgs_barrel_bending


import cv2
import os
import re
import time
import matplotlib.pyplot as plt

# 显示多张图片，输入可以是图片的url路径数组，也可以是图片对象
def showImages(images, titles=[], size=[1, 1], BGR=True):
    imgs_len = len(images)
    if len(titles) == 0:
        titles = ['']*imgs_len
    for i in range(imgs_len):
        plt.subplot(size[0], size[1], i + 1)
        showImage = images[i]
        if isinstance(showImage, str):
            showImage = cv2.imread(showImage)
        if (BGR):
            b, g, r = cv2.split(showImage)
            showImage = cv2.merge([r, g, b])
        plt.imshow(showImage, 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

# 显示一张图片，输入可以是图片的url路径，也可以是图片对象
def showImage(image):
    showImages([image])

# 提取字符串中的数字并转化成数字类型，用于排序
def sorted_key(value):
    return int(''.join(re.findall(r"\d+", value)))

# 根据文件夹自动生成文件夹下全部图片的路径
def get_imgs(dir):
    filenames = sorted(os.listdir(dir), key=sorted_key)
    return [os.path.join(dir, filename) for filename in filenames]

# 4种异常图像在移动硬盘中的文件夹，根据自己电脑中的文件夹路径进行替换
dir_line_pollution = '/Volumes/TOSHIBA EXT/图片素材库/硬盘素材库/项目/ZF项目/ZF电缆图像数据[v2蒋欣见]/线污染[v2]'
dir_line_damage = '/Volumes/TOSHIBA EXT/图片素材库/硬盘素材库/项目/ZF项目/ZF电缆图像数据[v2蒋欣见]/线损伤[v2]'
dir_barrel_pollution = '/Volumes/TOSHIBA EXT/图片素材库/硬盘素材库/项目/ZF项目/ZF电缆图像数据[v2蒋欣见]/筒污染[v2]'
dir_barrel_bending = '/Volumes/TOSHIBA EXT/图片素材库/硬盘素材库/项目/ZF项目/ZF电缆图像数据[v2蒋欣见]/筒弯曲[v2]'

# 根据文件夹路径，自动生成4种异常每个图片具体路径字符串数组
imgs_line_pollution = get_imgs(dir_line_pollution)
imgs_line_damage = get_imgs(dir_line_damage)
imgs_barrel_pollution = get_imgs(dir_barrel_pollution)
imgs_barrel_bending = get_imgs(dir_barrel_bending)

class Images(object):
    def __init__(self, line_pollution, line_damage, barrel_pollution, barrel_bending):
        self.line_pollution = line_pollution
        self.line_damage = line_damage
        self.barrel_pollution = barrel_pollution
        self.barrel_bending = barrel_bending

imgs = Images(imgs_line_pollution, imgs_line_damage, imgs_barrel_pollution, imgs_barrel_bending)
