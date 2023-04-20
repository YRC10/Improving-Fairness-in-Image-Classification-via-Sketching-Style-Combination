import cv2
import os

# input 218x178
# output 512x418 然后两边白色padding各47

inputpath = "./dataset/"
outputpath = "./dataset/"
color = 255
count = 0
sensitive_type = os.listdir(inputpath)
print(sensitive_type)
for st in sensitive_type:
    folder = os.listdir(inputpath+st+'/sketch/')
    for fold in folder:
        # print(img_list)
        img_list = os.listdir(inputpath+st+'/sketch/'+fold)
        for file in img_list:
            img_type = file.split('.')[1]
            if img_type != 'jpg':
                continue

            img = cv2.imread(inputpath+st+'/sketch/'+fold+'/'+file)
            img_name = file.split('.')[0]

            size = 256
            # 获取原始图像宽高。
            height, width = img.shape[0], img.shape[1]
            # size = max(height, width)

            # 等比例缩放尺度。
            scale = height/size
            # 获得相应等比例的图像宽度。
            width_size = int(width/scale)

            

            if (height == size) and (width == size):
                print('already resized image', count)
                continue
            else:
                # resize
                image_resize = cv2.resize(img, (width_size, size))
                # padding

                ret = cv2.copyMakeBorder(image_resize, int((size-image_resize.shape[0])/2), 
                                                    int((size-image_resize.shape[0])/2), 
                                                    int((size-image_resize.shape[1])/2), 
                                                    int((size-image_resize.shape[1])/2), 
                                                    
                                            cv2.BORDER_CONSTANT, 
                                            value=(color, color, color))

                cv2.imwrite(outputpath+st+'/sketch/'+fold+'/'+img_name+'.jpg', ret)

                # 删除原文件，视情况而定！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
                # os.remove(inputpath+'/'+file)
        count += 1


print(count)
# print('Done! Resized %d images in total' % count)
# print((image_resize.shape[0]))
# print((image_resize.shape[1]))
