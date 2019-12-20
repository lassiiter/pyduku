import cv2
import numpy as np

while True:
    sudoku = cv2.imread("sudoku.jpg",cv2.IMREAD_GRAYSCALE)
    width, height = sudoku.shape[:2]
    outerbox = sudoku
    sudoku = cv2.GaussianBlur(sudoku,(11,11),0)
    outerbox = cv2.adaptiveThreshold(sudoku,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    outerbox = cv2.bitwise_not(outerbox)
    kernel = np.ones((3,3),np.uint8)
    outerbox = cv2.dilate(outerbox,kernel,iterations=1)

    # finding largest blob
    
    max = -1
    mask = np.zeros(outerbox.shape[:-1],np.uint8)
    mask1 = np.zeros((height+2, width+2), np.uint8)

    for x in range (0,width):
        for y in range (0,height):
            if outerbox[x,y] >=128:
                area = cv2.floodFill(mask,mask1,(0,0),255) 
                if area > max:
                    max = area
    
    cv2.imshow('image',outerbox)

    key = cv2.waitKey(1)
    if key == 27:
        break





cv2.destroyAllWindows()