import cv2
import numpy as np
import pandas as pd


def delete_little_part(img,text_pixel_ratio:int=10,symbol_pixel_ratio:int=60,x_step:int=10,y_step:int=10,is_background_white:bool=True, crop_around:bool=True):
    #split image to sub boxes and delete some ratio part

    x_step:int=max(20,x_step)
    y_step:int=max(30,y_step)
    if img.shape[2]>1:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cleaned_img=img.copy()
    #cleaned_img=cv2.threshold(cleaned_img, 50, 255, cv2.THRESH_BINARY )
    for y in range(0,img.shape[0],y_step):
        for x in range(0,img.shape[1],x_step):
            black_count:int=0
            white_count:int=0
            if (x==0 or y==0 or (x in range(0,img.shape[1],x_step)[-1:]) or (y in range(0,img.shape[0],y_step)[-1:])) and (crop_around):
                if is_background_white:
                    cleaned_img[y:y+y_step,x:x+x_step]=255
                else:
                    cleaned_img[y:y+y_step,x:x+x_step]=0
            else:
                for j in range(y,y+y_step):
                    for i in range(x,x+x_step):
                        if j<img.shape[0] and i<img.shape[1]:
                            if img[j,i]>=250:
                                white_count +=1
                            elif img[j,i]<=10:
                                black_count +=1
                total_pixel=x_step*y_step
                b_w_ratio:float=black_count/total_pixel
                w_b_ratio:float=white_count/total_pixel
                if is_background_white:
                    if b_w_ratio<text_pixel_ratio/100 or b_w_ratio>symbol_pixel_ratio/100:
                        cleaned_img[y:y+y_step,x:x+x_step]=255
                elif ~is_background_white:
                    if w_b_ratio<text_pixel_ratio/100 or w_b_ratio>symbol_pixel_ratio/100:
                        cleaned_img[y:y+y_step,x:x+x_step]=0
    return cleaned_img