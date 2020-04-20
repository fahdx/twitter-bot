from selenium import webdriver
#
# # Access to Twitter
# url = r'https://twitter.com'
# driver = webdriver.Firefox()
# driver.get(url)

import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

import arabic_reshaper

# install: pip install python-bidi
from bidi.algorithm import get_display
from langdetect import detect

import sys
c=0
pos=20
b,g,r,a = 25,255,25,0
for i in range(8):
    img = cv2.imread('m2.jpg')
    x='فهد    يبيسسطسسيحبك هههههه'.encode('utf-8')
    #x=u'' + x.decode('utf-8')
    x= x.decode('utf-8')



    print(detect(x))
    x="ماهو لونك my book title was about sport story بمصسيبمل يسببلل "
    print(detect(x))

    exit(0)




    fontpath = "./arabic_fonts/AArghavan.ttf"
    font = ImageFont.truetype(fontpath, 50)

    #im = Image.open('m2.jpg')

    im=img

    im = np.array(im)






    im = Image.fromarray((im))

    reshaped_text = arabic_reshaper.reshape(x)  # correct its shape
    x = get_display(reshaped_text)


    draw = ImageDraw.Draw(im,)
    draw.text((50, 100),x,font=font  , fill=(b,g,r,a ))
    im = np.array(im)
    cv2.imwrite("res.jpg",im)
    # print(x)
    exit(0)






    cv2.putText(img,x , (1, pos), i, 1, (255, 255, 255), 2, cv2.FONT_HERSHEY_COMPLEX)
    cv2.imshow("img",img)


    pos+=40
    cv2.imwrite("out"+str(c)+".jpg", img)
    c+=1

#
# cv2.putText(img, 'FONT_HERSHEY_COMPLEX_SMALL', (1, pos),2, 1, (255, 255, 255), 2, cv2.FONT_HERSHEY_COMPLEX_SMALL)
# cv2.imshow("img",img)
#
#
#
# pos+=20
# cv2.imwrite("out"+str(c)+".jpg", img)
# c+=1
#
# cv2.putText(img, 'FONT_HERSHEY_DUPLEX', (1, pos), 3, 1, (255, 255, 255), 2, cv2.FONT_HERSHEY_DUPLEX)
# cv2.imshow("img",img)
#
#
# pos+=20
#
# cv2.imwrite("out"+str(c)+".jpg", img)
# c+=1
#
# cv2.putText(img, 'hFONT_HERSHEY_PLAINhhh', (1, pos), 4, 1, (255, 255, 255), 2, cv2.FONT_HERSHEY_PLAIN)
# cv2.imshow("img",img)
#
#
# pos+=20
#
# cv2.imwrite("out"+str(c)+".jpg", img)
# c+=1
#
# cv2.putText(img, 'hFONT_HERSHEY_SCRIPT_COMPLEXh', (1, pos), 5, 1, (255, 255, 255), 2, cv2.FONT_HERSHEY_SCRIPT_COMPLEX)
# cv2.imshow("img",img)
#
#
# pos+=20
#
# cv2.imwrite("out"+str(c)+".jpg", img)
# c+=1
#
# cv2.putText(img, 'hFONT_HERSHEY_SCRIPT_SIMPLEXhhh', (1, pos), 6, 1, (255, 255, 255), 2, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX)
# cv2.imshow("img",img)
#
#
# pos+=20
#
# cv2.imwrite("out"+str(c)+".jpg", img)
# c+=1
#
# cv2.putText(img, 'hFONT_HERSHEY_SIMPLEXh', (1, pos), 7, 1, (255, 255, 255), 2, cv2.FONT_HERSHEY_SIMPLEX)
# cv2.imshow("img",img)
#
#
# pos+=20
# cv2.imwrite("out"+str(c)+".jpg", img)
# c+=1
#
#
# cv2.putText(img, 'FONT_HERSHEY_SCRIPT_COMPLEXh', (1, pos), 0, 1, (255, 255, 255), 2, cv2.FONT_HERSHEY_TRIPLEX)
# cv2.imshow("img",img)
#
#
# pos+=20
#
# cv2.putText(img, 'FONT_HERSHEY_SCRIPT_COMPLEXh', (1, pos), 0, 1, (255, 255, 255), 2, cv2.FONT_HERSHEY_SCRIPT_COMPLEX)
# cv2.imshow("img",img)
#
#
#
# cv2.imwrite("out"+str(c)+".jpg", img)
# c+=1
#
#
#
#
#
#
