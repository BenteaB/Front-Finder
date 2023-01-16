import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image, ImageEnhance


def filterImage(image_path, colored):
    image = mpimg.imread(image_path)
    plt.imshow(image)
    plt.show()

    # Convert image to HSV colorspace
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_image)
    plt.show()

    red_mask = cv2.inRange(rgb_image, (254, 50, 0), (254, 50, 0))
    blue_mask = cv2.inRange(rgb_image, (0, 50, 254), (0, 50, 254))
    purple_mask = cv2.inRange(rgb_image, (229, 50, 229), (229, 50, 229))

    filtered = np.zeros_like(image, np.uint8)
    if (colored == True):
        imask = red_mask > 0
        filtered[imask] = image[imask]
        imask = blue_mask > 0
        filtered[imask] = image[imask]
        imask = purple_mask > 0
        filtered[imask] = image[imask]
    else:
        for x in range(rgb_image.shape[0]):
            for y in range(rgb_image.shape[1]):
                if (rgb_image[x, y] > 75).all():
                    rgb_image[x, y] = 255
        filtered = rgb_image

    filtered_img = cv2.cvtColor(filtered, cv2.COLOR_RGBA2RGB)

    if (colored == True):
        for x in range(filtered_img.shape[0]):
            for y in range(filtered_img.shape[1]):
                if (filtered_img[x, y] == 0).all():
                    filtered_img[x, y] = 255
                else:
                    filtered_img[x, y] = 0

    plt.imshow(filtered_img)
    plt.show()

    cv2.imwrite('data/filtered/cold/' + image_path + '-filtered.png', filtered_img)


def black_and_white(img_path, x):
    img = Image.open(img_path)
    img_data = img.getdata()
    lst=[]
    for i in img_data:
        # lst.append(i[0]*0.299+i[1]*0.587+i[2]*0.114) ### Rec. 609-7 weights
        lst.append(i[0]*0.2125+i[1]*0.7174+i[2]*0.0721) ### Rec. 709-6 weights
    new_img = Image.new("L", img.size)
    new_img.putdata(lst)
    new_img.save(x)


def main():
    type = ['cold', 'occluded', 'warm']
    for t in type:
        for root, _, files in os.walk('data/colored/' + t):
            n = 0
            for image_path in files:
                n += 1
                black_and_white("data/colored/" + t + "/" + image_path, "data/filtered/" + t + '/' + str(n) + 'n.png')
    # filterImage("data/filtered/cold/3.png", True)

# main()
black_and_white("data/colored/to_predict/1.png", "data/colored/to_predict/2.png")
# filterImage("front12_color.gif", True)
# filterImage("front12.gif", False)