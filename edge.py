import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

pic_path = './AJ_image/'
save_path = './edge/'
name_list = os.listdir(pic_path)


for indx, file_name in  enumerate(name_list):
    picture_path = pic_path+file_name
    img = cv2.imread(picture_path)
    ed = cv2.Canny(img, 0, 150) 
    save_name_path = save_path+file_name
    cv2.imwrite(save_name_path,ed)

