from numpy import *

from PIL import Image

import cv2


# ori_img & se : array ( gray level )
# ret_val: ret_img ( gray level )
def gray_dilation(ori_img,se):
    img_height = len(ori_img)
    img_width = len(ori_img[0])
    se_height = len(se)
    se_width = len(se[0])
    # create procedure imgs
    # each img based on (ori_img and 1 block of se)
    # size=ret_img
    pcd_imgs = []
    ret_height = img_height+se_height-1
    ret_width = img_width+se_width-1
    for i in range(se_height):
        for j in range(se_width):
            th_img = [[-inf]*ret_width for k in range(ret_height)]#init array
            for h in range(img_height):
                for w in range(img_width):
                    th_img[h+i][w+j] = ori_img[h][w]+se[i][j]
            pcd_imgs.append(th_img)
    # calculate MAX for each pixel
    ret_img = [[-inf]*ret_width for k in range(ret_height)]
    for h in range(ret_height):
        for w in range(ret_width):
            vals = []
            for item in pcd_imgs:
                vals.append(item[h][w])
            ret_img[h][w] = max(vals)
    return array(ret_img)

# ori_img & se : array ( gray level )
# ret_val: ret_img ( gray level )
def gray_erosion(ori_img,se):
    img_height = len(ori_img)
    img_width = len(ori_img[0])
    se_height = len(se)
    se_width = len(se[0])
    # create procedure imgs
    # each img based on (ori_img and 1 block of se)
    # size=ret_img
    pcd_imgs = []
    ret_height = img_height+se_height-1
    ret_width = img_width+se_width-1
    for i in range(se_height):
        for j in range(se_width):
            th_img = [[-inf]*ret_width for k in range(ret_height)]#init array
            for h in range(img_height):
                for w in range(img_width):
                    th_img[h+se_height-i-1][w+se_width-j-1] = ori_img[h][w]-se[i][j]
            pcd_imgs.append(th_img)
    # calculate MIN for each pixel
    ret_img = [[-inf]*ret_width for k in range(ret_height)]
    for h in range(ret_height):
        for w in range(ret_width):
            vals = []
            for item in pcd_imgs:
                vals.append(item[h][w])
            ret_img[h][w] = min(vals)
    w=se_width-1
    h=se_height-1
    return array(ret_img)[h:-h,w:-w]

ori_img=array([[0,1,0,0],[1,1,1,1],[0,1,1,0],[0,0,0,1]])
se=array([[0,1,0],[1,1,0]])
ret=gray_dilation(gray_erosion(ori_img,se),se)

##img2 = Image.fromarray(ori_img)
##
##se2 = Image.fromarray(se)
##
##tmp2 = cv2.dilate(ori_img,se)
##ret2 = cv2.dilate(Image.fromarray(cv2.erode(Image.fromarray(ori_img),se)),se)
