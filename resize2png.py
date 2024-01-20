import cv2
import numpy as np

SCENE = ["basketball", "benz", "bigbear", "bigsnow", "blueballoon", "chair", "drums", "hotdog", "invrender_chair", "lego", "mic", "redballoon2", "ship", "toycar", "toyhorse"]

for scene in SCENE:
    for i in range(200):
        img_path = f'./output/{scene}/{i}.ppm'
        img = cv2.imread(img_path)
        new_img = np.ones([800, 800, 3])
        new_img *= 255
        new_img = new_img.astype(np.uint8)
        new_img[16:784, :, :] = img

        img_half = cv2.resize(new_img, (0,0), fx=0.5, fy=0.5)
        cv2.imwrite(f'./output/{scene}/{i}.png', img_half)
