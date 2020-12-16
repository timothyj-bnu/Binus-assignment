import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def main():
    img = cv.imread('joan_mir.jpg', 0);
    edge1 = cv.Canny(img, 30, 100)
    edge2 = cv.Canny(img, 100, 200)

    titles = ['Original','Threshold 30-100','Threshold 100-200']
    images = [img,edge1,edge2]
    for i in range(3):
        plt.subplot(1, 3, i+1), plt.imshow(images[i], cmap='gray')
        plt.title(titles[i]), plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == '__main__':
    main()

