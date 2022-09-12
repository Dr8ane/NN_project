import numpy
import cv2
import imutils

image = cv2.imread('123.bmp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(3, 3), 0)

edges = cv2.Canny(gray, 10, 250)
cv2.imwrite("edges.jpg", edges)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("closed.jpg", closed)

cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)


total = 0
wall = 0
door_wall = 0
window_wall = 0

for c in cnts:
    p = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * p, True)
    if len(approx) == 4:
        cv2.drawContours(image, [approx], -1, (0, 0, 255), 4)
        total += 1
        wall +=1
    if len(approx) == 7:
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
        total += 1
        door_wall +=1
    if len(approx) == 8:
        cv2.drawContours(image, [approx], -1, (255, 0, 0), 4)
        total += 1
        window_wall +=1

print('total = ', total)
print('wall(red) = ', wall)
print('door_wall(green) = ', door_wall)
print('window_wall(blue) = ', window_wall)
cv2.imwrite("test_final.jpg", image)