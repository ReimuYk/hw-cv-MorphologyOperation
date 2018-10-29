# hw-cv-MorphologyOperation
assignment 1 of "Computer Vision"

## Files & APIs

### morphologyoperation.py

#### gray_dilation(ori_img,se)
- input:
    - ori_img: a numpy "array" type, stands for origin image(grey level)
    - se: a numpy "array" type, stands for structure element(se)
- output:
    - ret_img: a numpy "array" type, which is dilated from origin image(grey level)
- implement:
    1. **calculate ret_img size**. The size will be *larger* than the origin image because of the dilation, w(ret_img)=w(ori_img)+w(se)-1,so does the height.
    2. **create temp images**. Each image contains information of the whole ori_img and only one block of se. Each image has the same size as ret_img, and place the ori_img with the offset of se block coordinate and increase each block the value of se block. Leave the other blocks "-inf".
    3. **merge tmp images**. Each coordinate of ret_img has the value of the max value of temp images of the same coordinate.

#### gray_erosion(ori_img,se)
- input:
    - ori_img: a numpy "array" type, stands for origin image(grey level)
    - se: a numpy "array" type, stands for structure element(se)
- output:
    - ret_img: a numpy "array" type, which is erosed from origin image(grey level)
- implement:
    1. **calculate ret_img size**. The size will be *smaller* than the origin image because of the erosion, w(ret_img)=w(ori_img)-w(se)+1,so does the height.
    2. **create temp images**. Each image contains information of the whole ori_img and only one block of se. Each image has a similar size as dilation operation, and place the ori_img towards *lower right corner* with the offset of se block coordinate and increase each block the value of se block. Leave the other blocks "-inf".
    3. **merge tmp images**. Each coordinate of ret_img has the value of the min value of temp images of the same coordinate.
    4. **cut out "-inf sides"**. Simply discard the sides with value of "-inf"

#### bi_dilation(ori_img,se,center=None)
- input:
    - ori_img: a numpy "array" type, stands for origin image. In the implement, we consider 0 as 0, and non-0 as 1.
    - se: a numpy "array" type, stands for structure element(se)
    - center(optional): a turple like (a,b) or a list like [a,b] stands for the coordinate of the center of se.
- output:
    - ret_img: anumpy "array" type, which is binary dilated from origin image.
- implement:
    1. **calculate ret_img size**. The size will be *larger* than the origin image because of the dilation, w(ret_img)=w(ori_img)+w(se)-1,so does the height.
    2. **build ret_img**. For each pixel with the value of 1 in ori_img, we overlap the center of se on it and draw the pixel of ret_img on each 1 pixel of the overlapped se.

#### bi_erosion(ori_img,se,center=None)
- input:
    - ori_img: a numpy "array" type, stands for origin image. In the implement, we consider 0 as 0, and non-0 as 1.
    - se: a numpy "array" type, stands for structure element(se)
    - center(optional): a turple like (a,b) or a list like [a,b] stands for the coordinate of the center of se.
- output:
    - ret_img: anumpy "array" type, which is binary erosed from origin image.
- implement:
    1. **calculate ret_img size**. The size will be *smaller* than the origin image because of the erosion, w(ret_img)=w(ori_img)-w(se)+1,so does the height.
    2. **build ret_img**. We overlap the se on each appropriate place on ori_img, and check if each 1 pixel of se match a 1 pixel of ori_img. If true, draw the pixel of ret_img on corresponding place of se center.



