import cv2
import numpy as np

sudoku = cv2.imread('sudoku.jpg')
imgray = cv2.cvtColor(sudoku, cv2.COLOR_BGR2GRAY)
orig = imgray
outerbox = imgray
imgray = cv2.GaussianBlur(imgray,(11,11),0)
outerbox = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)
outerbox = cv2.bitwise_not(outerbox)
edges = cv2.Canny(outerbox,100,100)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

c = max(contours, key = cv2.contourArea)

#show green contour outline
showContours = cv2.drawContours(sudoku,c,-1,(0,255,0), 3)
cv2.imshow('contorus', showContours)

#try to find corner points
largestContour = cv2.drawContours(sudoku,c,-1,(0,255,0), 3)
cornersGrey = cv2.inRange(largestContour, (0,255,0), (0,255,0))
corners = cv2.goodFeaturesToTrack(cornersGrey, 4, .01, 50)
for i in corners:
    		x,y = i.ravel()
		cv2.circle(orig,(x,y),3,255,-1)
cv2.imshow('corners', orig)


#warp toward corners
pts1 = corners
print(corners)
pts2 = np.float32([[0,423],[419,0],[419,423],[0,0]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)

result = cv2.warpPerspective(orig,matrix,(419,423))
cv2.imshow('warp', result)

#

#kill on esc
cv2.waitKey(0)
cv2.destroyAllWindows()









