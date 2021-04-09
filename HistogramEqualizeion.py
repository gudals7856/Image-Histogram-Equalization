import cv2
import numpy as np

def histogramEqualization(img):
    height, width = img.shape
    level = 256
    pixels = height * width
    histogram = np.zeros(256)
    n_histogram = np.zeros(256)

    # 0~255까지 픽셀값을가진 픽셀의 개수를 구함(히스토그램 구하기)
    for x in range(width):  
        for y in range(height):
            i = img[y,x]
            histogram[i] = histogram[i] + 1

    # 히스토그램 normalize
    for i in range(level):
        n_histogram[i] = histogram[i]
        n_histogram[i] = float(n_histogram[i]) / pixels

    # CDF 구하기
    cdf = np.zeros(level)
    sum = 0
    
    for i in range(level):
        sum = sum + n_histogram[i]
        cdf[i] = sum * (level - 1)
        cdf[i] = round(cdf[i])

    # CDF 반올림하여 평활화된 히스토그램 구하기
    for x in range(width):
        for y in range(height):
            img[y,x] = cdf[img[y,x]]

    return img

in_image = cv2.imread('dgu_night.png', 0)  # img2numpy

cv2.imshow('Input Image', in_image)

out_image = histogramEqualization(in_image)
cv2.imshow('Result Image', out_image)

cv2.imwrite('dgu_night_equlization.png', out_image)  # save result img
cv2.waitKey()
