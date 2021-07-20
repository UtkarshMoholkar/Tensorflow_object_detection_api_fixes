import os
import cv2

list_of_files = os.listdir()
list_of_png = list(filter(lambda x:x.split(".")[-1]=="png", list_of_files))

for png_img in list_of_png:
    split_name = png_img.split(".")
    img_name = split_name[0]
    png_img = cv2.imread(png_img)
    cv2.imwrite(f'../{img_name}.jpg', png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

